#1- Imports
from dataclasses import dataclass, field
from typing import List

#2- Create a 'dataclass' for all configs that can be used anywhere in this Project
@dataclass
class AgenticAIConfig:
    # UI Selections from users
    provider:str = "OpenAI"
    model: str = "gpt-4o"
    temperature: float = 0.7
    max_tokens:int = 1000
    
    # User Input
    user_query:str=""
    
    # Agent Settings (CrewAI Specifics)
    agent_name:str = "default"
    tools: List[str] = field(default_factory=list)
    
    # Runtime
    response:str=""
    chat_history:List[dict] = field(default_factory=list)