from langchain_core.prompts import ChatPromptTemplate, PromptTemplate, MessagesPlaceholder

#chat template
chat_template = ChatPromptTemplate([
    ('SYSTEM', "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="history"),
    ('HUMAN', "What is the capital of Pakistan?")
])

#LOad Chat History
with open("chat_history.txt", "r") as f:
    chat_history = f.read()


#create Prompt
prompt = chat_template.format(history=chat_history)
