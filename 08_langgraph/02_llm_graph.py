### Code 18: LangGraph with an LLM

# Create `08_langgraph/02_llm_graph.py`.


# Code 18: LangGraph with an LLM

from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_ollama import ChatOllama


# Step 1: Initialize Ollama LLM
llm = ChatOllama(model="llama3.2:3b", temperature=0)


# Step 2: Define Agent State
class AgentState(TypedDict):
    question: str
    answer: str


# Step 3: Create AI Agent Node
def ai_agent(state: AgentState):
    response = llm.invoke(state["question"])

    return {"answer": response.content}


# Step 4: Create StateGraph
builder = StateGraph(AgentState)


# Step 5: Add AI Agent Node
builder.add_node("ai_agent", ai_agent)


# Step 6: Define Workflow
builder.add_edge(START, "ai_agent")
builder.add_edge("ai_agent", END)


# Step 7: Compile Graph
graph = builder.compile()


# Step 8: Execute Graph
result = graph.invoke(
    {
        "question": "Which skills i need to add to my genai resume in 2026 to get fresher jobs / calls?",
        "answer": "",
    }
)


# Step 9: Print Output
print("\n===== AI AGENT RESPONSE =====")
print(result["answer"])
