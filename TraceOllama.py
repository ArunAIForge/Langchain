from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama

# 1. Load LangSmith environment flags
load_dotenv()

# 2. Connect to the local Ollama instance (default: localhost:11434)
llm = ChatOllama(
    model="llama3.2:3b",
    temperature=0.7
)

# 3. Define the chain
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an experienced system architect. Give a concise explanation in 2 sentences."),
    ("human", "{question}")
])
chain = prompt | llm | StrOutputParser()

# 4. Invoke the chain
question = "Why does an asynchronous queue handle high write throughput better than synchronous DB writes?"
response = chain.invoke({"question": question})

print("\n--- Terminal Output ---")
print(response)
print("-----------------------\n")