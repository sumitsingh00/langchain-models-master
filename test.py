from langchain_openai import ChatOpenAI
# from langchain.schema import HumanMessage
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

# Fetch environment variables
api_key = os.getenv("OPENAI_API_KEY")
api_base = os.getenv("OPENAI_BASE_URL")
referer = os.getenv("HTTP_REFERER")
title = os.getenv("X_TITLE")

# Ensure required env vars are present
if not api_key or not api_base:
    raise Exception("Missing OPENAI_API_KEY or OPENAI_BASE_URL in .env")

# Create the ChatOpenAI client
llm = ChatOpenAI(
    model="openai/gpt-3.5-turbo-instruct",
    openai_api_key=api_key,
    openai_api_base=api_base,
    default_headers={
        "HTTP-Referer": referer,
        "X-Title": title,
    }
)


# Run the model
response = llm.invoke("What is the meaning of life?")

# Print the result
print(response.content)
