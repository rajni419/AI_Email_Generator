from langchain_core.output_parsers import StrOutputParser

from llm import llm
from prompt import email_prompt

# Output Parser
parser = StrOutputParser()

# LangChain Expression Language (LCEL) Chain
email_chain = email_prompt | llm | parser