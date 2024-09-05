from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
import dotenv
from third_parties.linkedIn import scrape_linkedIn_profile
import os

dotenv.load_dotenv()
if __name__ == "__main__":
    summary_prompt = """
    For the given linkedin data {data} give me one line joke about it"""
    OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
    summary_prompt_template = PromptTemplate(template=summary_prompt, input_variables = ['data'])
    llm = ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-3.5-turbo")

    linkedIn_data = scrape_linkedIn_profile(url=
                            "https://gist.githubusercontent.com/Aousaf90/4dff7a0e726b80a1ad77419a640aeb50/raw/daf0d6d4c981df9630c4929bd07997f56658fa76/gistfile1.txt")
    chain = summary_prompt_template | llm
    result = chain.invoke(input={"data": f"{linkedIn_data}"})
    print(f"Result: {result.content}")