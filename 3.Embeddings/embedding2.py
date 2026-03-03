from langchain_huggingface import HuggingFaceEmbeddings


embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

text = "What is the capital of Pakistan?"
result = embedding.embed_query(text)
print(f"Embedding dimensions: {len(result)}")
print(f"First 10 values: {result[:10]}")