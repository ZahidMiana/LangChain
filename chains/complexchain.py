from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

#prompt
prompt1 = PromptTemplate(
    template='Generate a Detailed report on {topic} with the following sections: Introduction, Key Findings, Conclusion',
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template='Based on the report generated in the previous step, create a concise summary that captures the main points and insights from {text}.',
    input_variables=[]
)

model = GoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.3)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({"topic": "Unemployment in Pakistan"})


print(result)
# chain.get_graph().print_ascii()  #visual form of  your chain