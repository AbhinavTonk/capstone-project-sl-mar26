#1- Imports
import streamlit as st
from dotenv import load_dotenv

from app_config.config import AgenticAIConfig

#2- Loading Env Variables
load_dotenv() # It will load all the Env Variables

#3- Set Page Config
st.set_page_config(
    page_title="Simplilearn Capstone", #Show it in the Tab
    page_icon="🤖",
    layout="wide"
)

#4- Initialize Config
if "config" not in st.session_state:
    st.session_state.config = AgenticAIConfig()
config = st.session_state.config
    
#5- Initialize Streamlit- Conversation History
if "chat_history" not in st.session_state:
    st.session_state.chat_history=[]

#6- Setting dict for Available Models
MODEL_REGISTRY={
    "OpenAI":["gpt-4.1","gpt-4o","gpt-4o-mini","gpt-3.5-turbo"],
    "Ollama":["llama3","mistral","phi3","gemma"]
}

#7- Creating Sidebar
with st.sidebar:
    st.title("LLM Configuration")
    config.provider = st.selectbox(
        "LLM Provider",
        list(MODEL_REGISTRY.keys())
    )
    
    #Dynamic Model Selection Logic
    available_models = MODEL_REGISTRY[config.provider]
    
    config.model = st.selectbox(
        "Model",
        available_models
    )
    
    config.temperature= st.slider(
        "Temperature",
        min_value=0.0,
        max_value=2.0,
        value=config.temperature,
        step=0.1
    )
    
    config.max_tokens=st.slider(
        "Max Tokens",
        min_value=100,
        max_value=4000,
        value=config.max_tokens,
        step=100
    )
    
    st.divider()
    
    # Display Current Configurations Separately
    st.subheader("Current Configuration:")
    
    st.write(f"**Provider:** {config.provider}")
    st.write(f"**Model:** {config.model}")
    st.write(f"**Temperature:** {config.temperature}")
    st.write(f"**Max Token:** {config.max_tokens}")


#8- Setting Page Title
st.title("🤖 Simplilearn Agentic AI Capstone")

#9- Creating User Input Section
config.user_query = st.text_area(
    "Enter your query here: ",
    value = config.user_query,
    height=200,
    placeholder = "Ask your question here..."
)
# Create Response Button
if st.button("Generate Response", type="primary"):
    if not config.user_query.strip():
        st.warning("Please enter a prompt before clicking the button")
    else:
        #Store the User Query for displaying in conversation History on Streamlit
        st.session_state.chat_history.append(
            {
                "role": "user",
                "message": config.user_query
            }
        )
        
        # Create a Spinner until response is generated
        with st.spinner("AI Agent is Thinking..."):
            # Call CrewAI FLow
            # TODO
            
            #Store the response for display in conversation history
            st.session_state.chat_history.append(
                {
                    "role": "assistant",
                    "message": config.response
                }
            )
            st.session_state.config= config
        

#10- Creating Response Section
st.subheader("Conversation History")

for chat in st.session_state.chat_history:
    if chat["role"]=="user":
        with st.chat_message("user"):
            st.write(chat["message"])
    else:
        with st.chat_message("assistant"):
            st.write(chat["message"])

#11- Creating the button for Users to clear all the chats from the UI
if st.sidebar.button("Clear Chat"):
    st.session_state.chat_history=[]
    st.rerun()