from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (
    create_react_agent,
    AgentExecutor 
)
from langchain import hub
import os
import dotenv

dotenv.load_dotenv()


def lookup(name: str)-> str:
    return  "Hello World"