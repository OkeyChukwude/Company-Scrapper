import os
import langchain
from langchain.llms import OpenAI, Cohere, HuggingFaceHub
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.agents import load_tools
from langchain.agents import initialize_agent

from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.document_loaders import TextLoader
from langchain.document_loaders import PyPDFLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

# from dotenv import load_dotenv

# basedir = os.path.abspath(os.path.dirname(__file__))
# load_dotenv(os.path.join(basedir, '.env'))  # take environment variables from .env.

# os.environ['OPENAI_API_KEY'] = os.environ.get('OPENAI_API_KEY')
# os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.environ.get("HUGGINGFACEHUB_API_TOKEN")
# os.environ["SERPAPI_API_KEY"] = os.environ.get("SERPAPI_API_KEY")

os.environ['OPENAI_API_KEY'] = "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"
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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 "
os.environ["SERPAPI_API_KEY"] = "569ae6e2daa82c1e8f874c249904baaffa496d80f0423122d56c673c7bae95f8"

gpt3 = OpenAI(model_name='text-davinci-003')

tool_names = ["serpapi"]
tools = load_tools(tool_names)

agent = initialize_agent(tools, llm =gpt3 , agent="zero-shot-react-description", verbose=True)

def scrape(company_name, country, url=None):
    try:
        answer = agent.run(f"What products/services does the company {company_name} offer?")
        return answer
    except:
        return 'There was an error. Try again!'


if __name__ == '__main__':
    answer = agent.run(f"What products/services does the company Google offer?")
    print(answer)