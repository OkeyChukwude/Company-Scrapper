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
from langchain.agents import AgentType
from langchain import SerpAPIWrapper
from langchain.docstore.document import Document
from langchain.chains.question_answering import load_qa_chain

# gpt3 = OpenAI(model_name='text-davinci-003')
ollm = OpenAI(temperature=0.7) #OpenAI LLM with a temperature of 0.7 increasing its creativity 

#The search tool used to search the internet
tool_names = ["serpapi"]
tools = load_tools(tool_names)

#Initializing the agent that uses the search tool and the openAI LLM to answer questions
agent = initialize_agent(tools, llm =ollm , agent="zero-shot-react-description", verbose=True)


def scrape(company_name, country, url=None):
    ''' 
    Function that takes in Company and country, 
    and searches the internet to get's the description and then gets 
    the products and services from the description as a commaseperated list. 

    Keyword arguments:
    company_name: str 
    country: str 

    Returns 
    (Description : str, products :str) : tuple
       
    '''
    try:
    
        description = agent.run(f"Which industry does the company called {company_name}  based in {country} operate in and list all the products and services they offer ?")
        docs1 = [Document(page_content=description)]
        query1 = "only give me a comma seperated list of the products and services offered that are related to the industry, with their complete names"
        chain = load_qa_chain(OpenAI(temperature=0), chain_type="stuff")
        products = chain.run(input_documents=docs1, question=query1)

        return (description,products)
        # return products
    except:
        return 'There was an error. Try again!'


if __name__ == '__main__':
    answer = agent.run(f"What products/services does the company Google offer?")
    print(answer)