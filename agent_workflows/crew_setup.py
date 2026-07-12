#1- Imports
from crewai import LLM, Agent, Crew, Task
from crewai.tools import tool
import os
import sqlite3

#2- DB COnnection to read the DB Data
connection=sqlite3.connect("db/products.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM products")
db_data = cursor.fetchall()
PRODUCT_DB ={
    name.lower():{
        "price":price,
        "stock":stock,
        "brand":brand
        } for _,name,price,stock,brand in db_data
}


#3- Creating Tool that will fetch the data from DB
@tool("product_db_tool")
def product_db_tool(product_name:str)->str:
    """
    Get Product details from the product database
    """
    product_name = product_name.lower()
    
    if product_name in PRODUCT_DB:
        return str(PRODUCT_DB[product_name])
    
    return "Product Not Found"

#4- CrewAI Specific Steps
def create_crew(config):
    #a) LLM Config
    llm=LLM(
        model=config.model,
        api_key=os.getenv("OPENAI_API_KEY") if config.provider == "OpenAI" else None,
        temperature=config.temperature
    )
    
    #b) Define Agents
    # i) Classifier Agent
    classifier_agent=Agent(
        role="Classifier Agent",
        goal="Classify user query into product or general",
        backstory="Expert at understanding the user intent",
        verbose=True,
        llm=llm
    )
    
    # ii) DB Agent
    db_agent=Agent(
        role="Database Agent",
        goal="""
        You must call product_db_tool.
        Never answer from your trained knowledge
        If the tool returns 'Product not found' then 
        you final answer must be : "Product Details are not available in the database"
        
        Provide the result strictly from DB only
        """,
        backstory="Fetch product information where query is product related",
        tools=[product_db_tool],
        verbose=True,
        llm=llm
    )
    
    # iii) Research Agent
    research_agent=Agent(
        role="Research Agent",
        goal="Research and Explain general Topics clearly. Strictly donot research for 'product' queries",
        backstory="Expert researcher",
        verbose=True,
        llm=llm
    )
    
    # iv) Writer Agent
    writer_agent=Agent(
        role="Writer Agent",
        goal="Convert information into structured answer. Keep the answer within 50 words",
        backstory="FOrmat the responses into clean numbered list",
        verbose=True,
        llm=llm
    )
    
    #c) Fetch User query from config
    query = config.user_query
    
    #d) Define Tasks
    classify_task = Task(
        description="Classify the following query into 'product' or 'general' : Query is {query}",
        expected_output="product or general",
        agent=classifier_agent
    )
    
    db_task = Task(
        description= """
        Fetch product info for: {query}
        If info is not present in the DB then respond - 'Product detail not find in the DB'
        Do not provide the general info based on your trained knowledge
        Provide the result strictly from DB only
        """,
        expected_output="product details from the product DB",
        agent=db_agent,
        context=[classify_task]
    )
    
    research_task= Task(
        description="Explain this topic: {query}",
        expected_output="explanation",
        agent=research_agent,
        context=[classify_task]
    )
    
    write_task = Task(
        description="Format the previous outputs into bullet points",
        expected_output="Final Structured answer",
        agent=writer_agent,
        context=[classify_task,db_task,research_task]
    )
    
    #e) Create the Crew
    crew= Crew(
        agents=[classifier_agent,db_agent,research_agent,writer_agent],
        tasks=[classify_task,db_task, research_task, write_task]
    )
    
    #f) Return crew instance
    return crew