from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
import dotenv
import os

dotenv.load_dotenv()
if __name__ == "__main__":
    summary_prompt = """
    For the given name {name} give me one line joke about it"""
    OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
    summary_prompt_template = PromptTemplate(template=summary_prompt, input_variables = ['name'])
    llm = ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-3.5-turbo")

    chain = summary_prompt_template | llm
    result = chain.invoke(input={"name": "Nawaz Sharif"})
    print(f"Result: {result.content}")