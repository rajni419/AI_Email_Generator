import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

print("GROQ_API_KEY:", os.getenv("GROQ_API_KEY"))

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7
)