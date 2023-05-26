import os
import langchain
import json 
from langchain.llms import OpenAI 
from langchain.agents import load_tools
from langchain.agents import initialize_agent, Tool
from langchain.utilities import GoogleSerperAPIWrapper

gpt3 = OpenAI(model_name='text-davinci-003', temperature =0) #OpenAI LLM with a temperature of 0 increasing its creativity/ randomness
# ollm = OpenAI(temperature=0.7) 

#The search tool used to search the internet
tool_names = ["serpapi"]
tools = load_tools(tool_names)

search = GoogleSerperAPIWrapper()
tools2 = [
    Tool(
        name="Intermediate Answer",
        func=search.run,
        description="useful for when you need to ask with search"
    )
]


#Initializing the agent that uses the search tool and the openAI LLM to answer questions
agent = initialize_agent(tools, llm =gpt3 , agent="zero-shot-react-description", verbose=True)

agent2 = initialize_agent(tools2, llm =gpt3 , agent="zero-shot-react-description", verbose=True)


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
        query = f'''
            I need you to answer some questions about the company in double  quotes ''{company_name}'' that is based in this country in angle brackets <{country}> :
            Before giving the answer to the questions check for the following:
            1 - Find out information about the Company and make a clear distinction between their products and services 
            2 - Check if they have products, if they don't have, just put no products 
            3 - Check if they have Services that can be listed in a one word comma seperated list, if they don't have, just put no services 

            Here are the questions
            1 - Provide no less than a two sentence description of the company, that focuses on the industry it operates in, its country, its products and services.
            2 - What are all the Products the company offers ?, output this in a one to two word comma seperated list.
            3 - What are all the Services the company offers ?, output this in a one to two word comma seperated list.
            4 - What are the key words associated with this company and its product ?, output not less than 3 words in a comma seperated list.

            Return a JSON object with the following keys: Description,Keywords, Products, Services, where the products and services are in a list and not a string object. 
            
            Make sure to use double quotes for the keys of the JSON object
            Make sure the description is not less than two sentences. 
            Make sure the services is a valid type of service that can be rendered by a company. 
        '''
    
        details = agent.run(query)
        
        details = json.loads(details)

        prod_s_codes = agent2.run(f'give me only the SIC code without any text for the products in this list {details["Products"]}  ')
        prod_n_codes = agent2.run(f'give me only the NAICS code without any text for the products in this list {details["Products"]}  ')

        
        # query2 = f'''
        # I need you to answer some questions about the values in the list in the double quotes ''{details["Products"]}'' : 

        # 1 - What are the SIC codes from SEC for all the values in the list 
        # 2 - What are the NAICS codes for all the values in the list

        # Return a python dictionary object with the following keys: SIC Products, NAICS Products, where all the values are in a list and not a string object.
        # Make sure to use double quotes for the keys of the JSON object
        # Make sure to find the codes for each value seperately.
        # Make sure you only return SIC and NAICS Codes in the Python dictionary, there should be no text in the values output
        # '''

        # prod_s_n_codes = agent.run(query2)

        # query3 = f'''
        # I need you to answer some questions about the values in the list in the double quotes ''{details["Services"]}'' : 

        # 1 - What are the SIC codes from SEC for all the values in the list 
        # 2 - What are the NAICS codes for all the values in the list

        # Return a python dictionary object with the following keys: SIC Service, NAICS Services, where all the values are in a list and not a string object.
        # Make sure to use double quotes for the keys of the JSON object
        # Make sure to find the codes for each value seperately.
        # Make sure you only return SIC and NAICS Codes in the Python dictionary, there should be no text in the values output
        # '''

        serv_s_codes = agent2.run(f'give me only the SIC code without any text for the services in this list {details["Services"]}')
        serv_n_codes = agent2.run(f'give me only the NAICS code without any text for the services in this list {details["Services"]}')

        return (details, prod_s_codes, prod_n_codes, serv_n_codes, serv_s_codes)
        
    except Exception as e:
        print(e)
        return 'There was an error. Try again!'


if __name__ == '__main__':
    answer = agent.run(f"What products/services does the company Google offer?")
    print(answer)
