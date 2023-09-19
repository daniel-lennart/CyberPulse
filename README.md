# Cyber Pulse: NewsAPI Query Interface

Cyber Pulse is a Streamlit-based interface that allows users to interact with the NewsAPI using natural language queries. The application is powered by the Langchain library, which leverages OpenAI's GPT-3.5 Turbo model to interpret and generate API requests based on user input.

## Features

- **Natural Language Queries**: Users can enter natural language queries to fetch news articles. For example, "Fetch 10 articles related to malware".

- **Dynamic API Responses**: The application displays the response from the NewsAPI based on the user's query.


## Setup and Installation

1. Ensure you have Python installed on your system.

2. Clone this repository.

3. Navigate to the project directory and install the required libraries: `streamlit`, `langchain`, and `openai`.

4. Set up your NewsAPI key as an environment variable.

5. Run the Streamlit app.

6. Open the provided link in your browser to access the Cyber Pulse interface.

## Usage

1. Launch the Cyber Pulse interface.

2. Enter your natural language query in the provided text box. Here are some example queries you can use:

   - "Fetch 10 articles related to malware. Print article names as list."
   - "Show me the latest 5 articles about ransomware attacks. Print links to article, name and date published"
   - "Retrieve articles from the last week about cyber espionage."
   - "Find news articles written in English about OSINT tools from the past month."
   - "Get the top 3 most relevant articles about cyber threat intelligence."

3. Click the "Fetch Data" button.

4. View the processed API response displayed below.

