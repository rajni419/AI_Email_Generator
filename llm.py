from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

# Initialize the Groq LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7
)