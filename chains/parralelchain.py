from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()


model1 = GoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.3)

model2 = GoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.4)


prompt1 = PromptTemplate(
    template="Generate a short and simple notes on the following text \n {text} ",
    input_variables=["text"]
)

prompt2 = PromptTemplate(
    template="Based on the notes generate 3 short answer and question from following \n {text}",
    input_variables=["text"]
)

prompt3 = PromptTemplate(
    template="Merge the provided notes and questions into a single comprehensive summary that captures the key points and insights from both. \n Notes: {notes} \n Questions: {questions}",
    input_variables=["notes", "questions"]
)

parser = StrOutputParser()


parralel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'questions': prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parralel_chain | merge_chain

result = chain.invoke({"text": "The capital of Pakistan is Islamabad. It is known for its high standard of living, safety, and abundant greenery. The city is home to many parks and forests, making it a pleasant place to live. Islamabad also has a rich cultural heritage, with several museums and art galleries showcasing the history and culture of Pakistan."})

print(result)