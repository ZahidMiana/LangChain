from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

cla = ChatAnthropic(model="claude-2", temperature=0.7)  

result = cla.invoke("suggest me five pakistani food?")
print(result.content)