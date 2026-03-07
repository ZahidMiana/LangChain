from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from langchain_core.runnables import RunnableParallel, RunnableBranch,RunnableLambda


load_dotenv()

model1 = GoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.3)


parser = StrOutputParser()

class SentimentResult(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(..., description="The sentiment of the text")


parser2 = PydanticOutputParser(pydantic_object=SentimentResult)

prompt1 = PromptTemplate(
    template='classify the sentiment of the following text into positive or negative: {text} \n {format_instructions}',
    input_variables=["text"],
    partial_variables={"format_instructions": parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model1 | parser2

prompt2 = PromptTemplate(
    template='Write appropriate response to the positive feedback \n {text}',
    input_variables=["text"]
)

prompt3 = PromptTemplate(
    template='Write appropriate response to the negative feedback \n {text}',
    input_variables=["text"]
)


branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "positive", prompt2 | model1),
    (lambda x: x.sentiment == "negative", prompt3 | model1),
    RunnableLambda(lambda x: "Invalid sentiment")
)

chain = classifier_chain | branch_chain

print(chain.invoke({"text": "I love this product! It has exceeded my expectations."}))