from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

# Using a small model that can run locally
llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    pipeline_kwargs={
        "max_new_tokens": 100,
        "temperature": 0.7,
    }
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("Capital of Pakistan")
print(result.content)

