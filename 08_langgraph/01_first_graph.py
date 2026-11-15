# 9. Level 7 – LangGraph (very important)

# High-priority interview skill
# LangGraph is used to build stateful, controllable agent workflows.

# Learn:

# 1. StateGraph.
# 2. Nodes.
# 3. Edges.
# 4. Conditional edges.
# 5. Cycles and loops.
# 6. ToolNode.
# 7. Checkpointing.
# 8. Human-in-the-loop.
# 9. Multi-agent orchestration.
# 10. Persistent state.

# Install: pip install langgraph langchain-ollama

### Code 17: First LangGraph application

# Create `08_langgraph/01_first_graph.py`.


from typing import TypedDict
from langgraph.graph import StateGraph, START, END


# 1. Define Agent State
class AgentState(TypedDict):
    question: str
    answer: str


# 2. Define Assistant Node
def assistant(state: AgentState) -> dict:
    question = state["question"]

    return {"answer": "You asked: " + question}


# 3. Create StateGraph
builder = StateGraph(AgentState)


# 4. Add Node
builder.add_node("assistant", assistant)


# 5. Connect Nodes
builder.add_edge(START, "assistant")
builder.add_edge("assistant", END)


# 6. Compile Graph
graph = builder.compile()


# 7. Execute Graph
result = graph.invoke({"question": "What is LangGraph?", "answer": ""})


# 8. Display Result
print("\n===== LANGGRAPH OUTPUT =====")
print(result["answer"])
