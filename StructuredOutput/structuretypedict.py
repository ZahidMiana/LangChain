from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = GoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)   

class Review(TypedDict):
    summary: str
    sentiment: str

structured_model = model.with_structured_output(Review)



result = structured_model.invoke("Review the movie Inception and provide a summary and sentiment analysis in the form of a structured output.")
print(result)
print("Summary:", result.summary)
print("Sentiment:", result.sentiment)