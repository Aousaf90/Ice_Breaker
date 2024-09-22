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
from langchain_community.tools.tavily_search import TavilySearchResults
dotenv.load_dotenv()


def get_tavily_linkedIn_url(name: str):
    tavily_serach = TavilySearchResults()
    result = tavily_serach.run(name)
    return result

def lookup(name: str)-> str:
    try:
        llm = ChatOpenAI(
            model= "gpt-3.5-turbo",
            api_key=os.environ['OPENAI_API_KEY'],
            temperature=0
        )
        tempplate =  """given the full name {name_of_person} I want you to get it me a link to there linkedin profile page
                    Your answer should only contain only the URL"""
        prompt_template = PromptTemplate(template=tempplate, input_variables=["name_of_person"])
        tool_for_agents = [
            Tool(
                name= "Crowl google 4 linkedin profile page",
                func=get_tavily_linkedIn_url,
                description="useful when you need get the linkedin profile page"
            )
        ]
        react_prompt = hub.pull("hwchase17/react")
        agent = create_react_agent(tools=tool_for_agents, llm=llm, prompt=react_prompt)
        agent_executor = AgentExecutor(verbose=True, agent=agent, tools=tool_for_agents)
        result = agent_executor.invoke(
            input={"input": prompt_template.format_prompt(name_of_person=name)}
        )
        linked_in_profile_url = result['output']
        return linked_in_profile_url
    except Exception as e:
        print(f"Error: {e}")
        return ""


if __name__ == '__main__':
    name = input("Entr your name: ")
    result = lookup(name)
    print(f"Result: {result}")
