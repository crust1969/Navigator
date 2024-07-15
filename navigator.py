import streamlit as st
import requests
import openai

# Function to get outside business insights from Spiegel Online
def get_outside_insights():
    url = "https://newsapi.org/v2/everything?sources=spiegel-online&apiKey=YOUR_NEWSAPI_KEY"  # Replace with your NewsAPI key
    try:
        response = requests.get(url)
        response.raise_for_status()
        articles = response.json().get("articles", [])
        return articles
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching news: {e}")
        return []

# Function to get inside business content
def get_inside_content():
    return [
        {"title": "Quarterly Report", "content": "Details of the quarterly performance..."},
        {"title": "Employee Satisfaction Survey", "content": "Results of the latest survey..."}
    ]

# Function to ask LLM
def ask_llm(question, api_key):
    openai.api_key = api_key
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=question,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        st.error(f"Error querying OpenAI: {e}")
        return "Sorry, I couldn't process your request."

# Streamlit app
st.sidebar.title("Business Navigator")
page = st.sidebar.selectbox("Choose a page", ["Outside Insights", "Inside Content", "Ask LLM"])

if page == "Outside Insights":
    st.title("Outside Business Insights")
    articles = get_outside_insights()
    for article in articles:
        st.subheader(article.get("title", "No Title"))
        st.write(article.get("description", "No Description"))
        if article.get("url"):
            st.markdown(f"[Read more]({article['url']})")

elif page == "Inside Content":
    st.title("Inside Business Content")
    contents = get_inside_content()
    for content in contents:
        st.subheader(content["title"])
        st.write(content["content"])

elif page == "Ask LLM":
    st.title("Ask a Large Language Model")
    api_key = st.text_input("Enter your OpenAI API key:", type="password")
    question = st.text_input("Ask a question:")
    if api_key and question:
        answer = ask_llm(question, api_key)
        st.write(answer)
