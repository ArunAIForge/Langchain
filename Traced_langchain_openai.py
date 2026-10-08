from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

prompts = [
    "What is asynchronous processing?",
    "Explain REST API in simple terms.",
    "What are the SOLID principles in C#?"
]

for i, prompt in enumerate(prompts, start=1):
    response = llm.invoke(
        [HumanMessage(content=prompt)]
    )

    print(f"\n--- Prompt {i} ---")
    print(f"Question: {prompt}")
    print(f"Answer: {response.content}")