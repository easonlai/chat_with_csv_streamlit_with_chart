# Import necessary libraries.
import openai
from langchain.llms import AzureOpenAI
from langchain.agents import create_pandas_dataframe_agent
import pandas as pd

# Configure the baseline configuration of the OpenAI library for Azure OpenAI Service.
OPENAI_API_KEY = "PLEASE_ENTER_YOUR_OWNED_AOAI_SERVICE_KEY"
OPENAI_API_BASE = "https://PLESAE_ENTER_YOUR_OWNED_AOAI_RESOURCE_NAME.openai.azure.com/"
OPENAI_DEPLOYMENT_NAME = "PLEASE_ENTER_YOUR_OWNED_AOAI_GPT_MODEL_NAME"
OPENAI_MODEL_NAME = "text-davinci-003"
OPENAI_API_VERSION = "2023-05-15"
OPENAI_API_TYPE = "azure"
openai.api_key = OPENAI_API_KEY
openai.api_base = OPENAI_API_BASE
openai.api_version = OPENAI_API_VERSION
openai.api_type = OPENAI_API_TYPE

# Define a function to create Pandas DataFrame agent from a CSV file.
def create_pd_agent(filename: str):
    # Initiate a connection to the LLM from Azure OpenAI Service via LangChain.
    llm = AzureOpenAI(openai_api_key=OPENAI_API_KEY, 
                      deployment_name=OPENAI_DEPLOYMENT_NAME, 
                      model_name=OPENAI_MODEL_NAME, 
                      openai_api_version=OPENAI_API_VERSION,
                      openai_api_type=OPENAI_API_TYPE)

    # Read the CSV file into a Pandas DataFrame.
    df = pd.read_csv(filename)

    # Create a Pandas DataFrame agent from the CSV file.
    return create_pandas_dataframe_agent(llm, df, verbose=False)

# Define a function to query the agent.
def query_pd_agent(agent, query):
    prompt = (
        """
        You must need to use matplotlib library if required to create a any chart.

        If the query requires creating a chart, please save the chart as "./chart_image/chart.png" and "Here is the chart:" when reply as follows:
        {"chart": "Here is the chart:"}

        If the query requires creating a table, reply as follows:
        {"table": {"columns": ["column1", "column2", ...], "data": [[value1, value2, ...], [value1, value2, ...], ...]}}
        
        If the query is just not asking for a chart, but requires a response, reply as follows:
        {"answer": "answer"}
        Example:
        {"answer": "The product with the highest sales is 'Minions'."}
        
        Lets think step by step.

        Here is the query: 
        """
        + query
    )

    # Run the agent with the prompt.
    response = agent.run(prompt)

    # Return the response in string format.
    return response.__str__()
