from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

mmodel = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.3)

prompt = PromptTemplate(
    template='Write summary for the folfowung \n {poem}',
    input_variables=["poem"]
)

parser = StrOutputParser()

loader = TextLoader("../../cricket.txt", encoding="utf-8")

documents = loader.load()

print(documents)
print(len(documents))
print(documents[0].page_content)
print(documents[0].metadata)


chain = prompt | mmodel | parser
result = chain.invoke({"poem": documents[0].page_content})
print(result)