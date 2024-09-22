from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
import dotenv
from third_parties.linkedIn import scrape_linkedIn_profile
from agents.linkedIn_agents import lookup
import os


def ice_beaak_with(name: str):
    lookup_url = lookup(name)
    linkedIn_url = "https://gist.githubusercontent.com/Aousaf90/4dff7a0e726b80a1ad77419a640aeb50/raw/daf0d6d4c981df9630c4929bd07997f56658fa76/gistfile1.txt"
    linkedIn_data = scrape_linkedIn_profile(linkedIn_url)
    print(f"LinkedIn URL: {linkedIn_url}")
    return linkedIn_data

dotenv.load_dotenv()
if __name__ == "__main__":
    summary_prompt = """
    For the given linkedin data {data} give me some interested facts about the person
    the information will help me get started with the conversation"""
    OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
    summary_prompt_template = PromptTemplate(template=summary_prompt, input_variables = ['data'])
    llm = ChatOpenAI(
        api_key=OPENAI_API_KEY,
        model="gpt-3.5-turbo")
    linkedIn_data = ice_beaak_with("Aousaf Sulaman Multan")
    chain = summary_prompt_template | llm
    result = chain.invoke(input={"data": f"{linkedIn_data}"})
    print(f"Result: {result.content}")
