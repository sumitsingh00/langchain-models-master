from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from langchain_community.chat_models import ChatOpenAI
import os

# ✅ Set environment variables (optional)
os.environ["OPENAI_API_KEY"] = "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"
os.environ["OPENAI_BASE_URL"] = "https://openrouter.ai/api/v1"

# ✅ Create ChatOpenAI instance for OpenRouter
llm = ChatOpenAI(
    model="openai/gpt-3.5-turbo-instruct",   # Or "gpt-3.5-turbo" for chat models
    openai_api_key=os.environ["OPENAI_API_KEY"],
    openai_api_base=os.environ["OPENAI_BASE_URL"],
)

# ✅ Ask a question
messages = [HumanMessage(content="What is the meaning of life?")]
response = llm.invoke(messages)

# ✅ Output the result
print(response.content)
