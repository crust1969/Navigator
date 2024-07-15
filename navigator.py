import streamlit as st
import requests
import openai

# Set up OpenAI API key
openai.api_key = "sk-proj-8c1uMhGWphhxqXPXYOMYT3BlbkFJOXwM8ZwZFWd1TNYsUofO"

# Function to get outside business insights
def get_outside_insights():
    url = "https://newsapi.org/v2/everything?q=business&apiKey=YOUR_API_KEY"
    response = requests.get(url)
    articles = response.json().get("articles", [])
    return articles

# Function to get inside business content
def get_inside_content():
    return [
        {"title": "Quarterly Report", "content": "Details of the quarterly performance..."},
        {"title": "Employee Satisfaction Survey", "content": "Results of the latest survey..."}
    ]

# Function to ask LLM
def ask_llm(question):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Streamlit app
st.sidebar.title("Business Navigator")
page = st.sidebar.selectbox("Choose a page", ["Outside Insights", "Inside Content", "Ask LLM"])

if page == "Outside Insights":
    st.title("Outside Business Insights")
    articles = get_outside_insights()
    for article in articles:
        st.subheader(article["title"])
        st.write(article["description"])
        st.write(f"Read more")

elif page == "Inside Content":
    st.title("Inside Business Content")
    contents = get_inside_content()
    for content in contents:
        st.subheader(content["title"])
        st.write(content["content"])

elif page == "Ask LLM":
    st.title("Ask a Large Language Model")
    question = st.text_input("Ask a question:")
    if question:
        answer = ask_llm(question)
        st.write(answer)
