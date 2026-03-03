from langchain_google_genai import GeminiEmbedding
from dotenv import load_dotenv
load_dotenv()


embedding = GeminiEmbedding(model="gemini-2.5-flash", dimensions=32)

result = embedding.embed_query("What is the capital of Pakistan?")   
print(str(result))