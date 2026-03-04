from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st 
from dotenv import load_dotenv

load_dotenv()


model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

st.header("Research Tools")

user = st.text_input("Enter your query here")

if st.button("Summarize"):
    result = model.invoke(user)
    st.write(result.content)
