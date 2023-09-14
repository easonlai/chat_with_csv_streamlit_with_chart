# Import necessary libraries.
import streamlit as st
import pandas as pd
import json
from agent import create_pd_agent, query_pd_agent

def decode_response(response: str) -> dict:
    return json.loads(response)

def write_response(response_dict: dict):
    # Check if the response is an answer.
    if "answer" in response_dict:
        st.write(response_dict["answer"])

    # Check if the response is a bar chart.
    if "chart" in response_dict:
        st.image("./chart_image/chart.png")

    if "table" in response_dict:
        data = response_dict["table"]
        df = pd.DataFrame(data["data"], columns=data["columns"])
        st.table(df)

st.title("🤔 Chat with your CSV 📊")

st.write("Please upload your CSV and metadata file below.")

# Function to allow users to upload a CSV file.
csv_data = st.file_uploader("Upload your CSV file.")

# Function to allow users to input a query.
query = st.text_area("Please let me know your query.")

if st.button("Submit Query", type="primary"):
    # Create an agent from the CSV file.
    agent = create_pd_agent(csv_data)

    # Query the agent.
    response = query_pd_agent(agent=agent, query=query)

    # Decode the response.
    decoded_response = decode_response(response)

    # Write the response to the Streamlit app.
    write_response(decoded_response)
