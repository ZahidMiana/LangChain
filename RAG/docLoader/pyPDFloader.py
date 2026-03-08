from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("cricket.pdf")

docs = loader.load()

if not docs:
    print("No documents loaded. Check if the PDF path is correct.")
else:
    print(docs)
    print(len(docs))