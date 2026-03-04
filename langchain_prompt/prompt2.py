from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st 
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate, PromptTemplate


load_dotenv()


model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

st.header("Research Tools")

paper_input = st.selectbox( "Select Research Paper Name",["Attention is all you need", "BERT", "GPT-3 Language model", "Diffusion model Beat Gan's on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] )

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )



# template
template = PromptTemplate(
    template="""
Please summarize the research paper titled "{paper_input}" with the following specification
Explanation Style: {style_input}
Explanation Length: {length_input}
1. Mathematical Details:
   - Include relevant mathematical equations if present in the paper.
   - Explain the mathematical concepts using simple, intuitive code snippets where
applicable.
2. Analogies:
   - Use relatable analogies to simplify complex ideas.
""",
    input_variables=["paper_input", "style_input", "length_input"]
)

prompt = template.invoke({
    "paper_input": paper_input,
    "style_input": style_input,
    "length_input": length_input
})


if st.button("Summarize"):
    result = model.invoke(prompt)
    st.write(result.content)

