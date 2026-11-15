### Code 15: LangChain prompt template

# Create `07_langchain/02_prompt_template.py`.
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

# Step 1: Initialize the Ollama LLM
llm = ChatOllama(model="llama3.2:3b", temperature=0)

# Step 2: Create the prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an Agentic AI interview expert."),
        ("human", "Explain {topic} with questions and answers and Python examples."),
    ]
)

# Step 3: Create the LangChain pipeline
chain = prompt | llm

# Step 4: Execute the chain
llm_result = chain.invoke({"topic": "AI Agent Tools"})

# Step 5: Print the response
print(llm_result.content)
