### Code 20: LangGraph with loops

# Create `08_langgraph/04_agent_loop.py`.


# Code 04: Agent Loop using LangGraph

from typing import TypedDict
from langgraph.graph import StateGraph, START, END


# Step 1: Define State
class State(TypedDict):
    count: int


# Step 2: Create Increment Node
def increment(state: State):
    return {"count": state["count"] + 1}


# Step 3: Create Conditional Function
def continue_loop(state: State):
    if state["count"] < 5:
        return "increment"

    return "finish"


# Step 4: Create StateGraph
builder = StateGraph(State)


# Step 5: Add Node
builder.add_node("increment", increment)


# Step 6: Add Starting Edge
builder.add_edge(START, "increment")


# Step 7: Add Conditional Edges
builder.add_conditional_edges(
    "increment", continue_loop, {"increment": "increment", "finish": END}
)


# Step 8: Compile Graph
graph = builder.compile()


# Step 9: Execute Graph
result = graph.invoke({"count": 0})


# Step 10: Print Result
print("\n===== LANGGRAPH LOOP OUTPUT =====")
print("Final Count:", result["count"])


# Expected result: {'count': 5}
# This is the foundation for agents that repeatedly plan,
# execute, observe, and retry.
