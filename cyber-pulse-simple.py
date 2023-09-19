# Import necessary libraries
import streamlit as st
import os
from langchain.chat_models import ChatOpenAI
from langchain.chains import APIChain
import datetime
import sys
from io import StringIO

# Retrieve the API key from environment variables
NEWSAPI_KEY = os.environ.get("NEWSAPI_KEY")
if not NEWSAPI_KEY:
    st.error("NewsAPI key not found in environment variables!")

# Define the News API documentation
NEWS_API_DOCS = """
    BASE URL: https://newsapi.org/v2

    API Documentation:
    The News API provides access to the latest news articles from various sources.
    The main endpoints include the top headlines, everything, and sources.

    Endpoints:
    - everything:
        path: /everything
        method: GET
        params: q, qInTitle, sources, domains, excludeDomains, from, to, language, sortBy, pageSize, page
"""

# Initialize the OpenAI LLM
llm = ChatOpenAI(model="gpt-3.5-turbo-16k", temperature=0.3)

# Set the headers for the API request
headers = {"x-api-key": NEWSAPI_KEY}

# Create the APIChain for NewsAPI with the headers
chain = APIChain.from_llm_and_api_docs(llm, NEWS_API_DOCS, headers=headers, verbose=True)

# Streamlit app
st.title("Cyber Pulse: NewsAPI Query Interface")
st.write("Enter Natural Language API query:")
st.write("Example: Fetch 10 articles related to malware. Print article names as list")

# User input
user_query = st.text_input("Your Query:")

# Button to run the query
if st.button("Fetch Data"):
    params = {
       
    }
    question = user_query + "do not add apiKey parameter. date today is " + str(datetime.date.today())

    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    # Restore stdout and get the captured URL
    sys.stdout = old_stdout
    generated_url = new_stdout.getvalue().strip()
    
    # Display the captured URL in Streamlit
    st.write("Generated API URL:")
    st.write(generated_url)
    response = chain.run(question=question, params=params)
    
    st.write("API Response:")
    st.write(response)

