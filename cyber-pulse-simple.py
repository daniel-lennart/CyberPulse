# Import necessary libraries
from typing import Dict, Any, Optional
from langchain.callbacks.manager import CallbackManagerForChainRun
from pydantic import BaseModel, Extra
import streamlit as st
import os
from langchain.chat_models import ChatOpenAI
from langchain.chains import APIChain
import datetime
import sys
from io import StringIO

class CustomAPIChain(APIChain):
    class Config:
        extra = Extra.allow

    _last_api_url: Optional[str] = None

    def _call(self, inputs: Dict[str, Any], run_manager: Optional[CallbackManagerForChainRun] = None) -> Dict[str, str]:
        _run_manager = run_manager or CallbackManagerForChainRun.get_noop_manager()
        question = inputs[self.question_key]
        api_url = self.api_request_chain.predict(
            question=question,
            api_docs=self.api_docs,
            callbacks=_run_manager.get_child(),
        )
        _run_manager.on_text(api_url, color="green", end="\n", verbose=self.verbose)
        self._last_api_url = api_url.strip()
        api_response = self.requests_wrapper.get(self._last_api_url)
        _run_manager.on_text(
            api_response, color="yellow", end="\n", verbose=self.verbose
        )
        self._last_api_response = api_response
        answer = self.api_answer_chain.predict(
            question=question,
            api_docs=self.api_docs,
            api_url=self._last_api_url,
            api_response=self._last_api_response,
            callbacks=_run_manager.get_child(),
        )
        return {self.output_key: answer}

    @property
    def last_api_url(self):
        return self._last_api_url

    @property
    def last_api_response(self):
        return self._last_api_response



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
chain = CustomAPIChain.from_llm_and_api_docs(llm, NEWS_API_DOCS, headers=headers, verbose=True)

# Streamlit app layout and styling
st.title("Cyber Pulse: NewsAPI Query Interface")
st.write("## Enter Natural Language API query:")
st.write("Example: Fetch 10 articles related to malware. Print article names as list")


# User input
user_query = st.text_input("Your Query:")

# Button to run the query
if st.button("Fetch Data"):
    params = {}
    question = user_query + "do not add apiKey parameter. date today is " + str(datetime.date.today())
    response = chain.run(question=question, params=params)
    
    # Display API URL
    st.write("## API URL:")
    st.write(f"`{chain.last_api_url}`")
    
    # Display Raw API Data
    st.write("## API Raw Data:")
    st.text_area("", chain.last_api_response, height=200)  # set a fixed height for better layout
    
    # Display API Response
    st.write("## API Response:")
    st.write(response)

# Add some spacing at the bottom for cleaner look
st.write("\n\n")


