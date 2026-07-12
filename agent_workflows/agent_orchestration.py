#1- Imports
from langsmith import traceable

from agent_workflows.crew_setup import create_crew
from app_config.config import AgenticAIConfig
from observability.logger import logger


#2- Langsmith Specific
@traceable(name="SL Agentic AI Capstone Demo", run_type="chain")
def run(config: AgenticAIConfig):
    """
    Main Entry Point of Agentic AI Workflow
    """
    logger.info("Agentic Workflow Started...")
    # Call CrewAI specific steps
    crew = create_crew(config) #TODO
    
    result = crew.kickoff(
        inputs={
            "query": config.user_query
        }
    )
    
    config.response=str(result)
    
    return config
    