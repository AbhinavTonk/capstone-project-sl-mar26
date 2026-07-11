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

#7- Creating Sidebar

#8- Setting Page Title

#9- Creating User Input Section

#10- Creating Response Section

#11- Creating the button for Users to clear all the chats from the UI