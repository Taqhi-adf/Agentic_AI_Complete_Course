### Code 21: Human-in-the-loop approval

# Create `08_langgraph/05_human_approval.py`.


# Code 05: Human Approval using LangGraph

from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import interrupt, Command


# Step 1: Define State
class State(TypedDict):
    action: str
    approval: str


# Step 2: Create Human Approval Node
def approval_node(state: State):
    decision = interrupt(f"Approve this action? {state['action']}")

    return {"approval": decision}


# Step 3: Create Execution Node
def execute_node(state: State):
    if state["approval"].lower() == "yes":
        return {"approval": "Approved and executed"}

    return {"approval": "Rejected; not executed"}


# Step 4: Create StateGraph
builder = StateGraph(State)


# Step 5: Add Nodes
builder.add_node("approval", approval_node)
builder.add_node("execute", execute_node)


# Step 6: Define Workflow
builder.add_edge(START, "approval")
builder.add_edge("approval", "execute")
builder.add_edge("execute", END)


# Step 7: Create Memory Checkpointer
memory = InMemorySaver()


# Step 8: Compile Graph
graph = builder.compile(checkpointer=memory)


# Step 9: Configure Thread ID
config = {"configurable": {"thread_id": "approval_001"}}


# Step 10: Execute Graph
result = graph.invoke(
    {"action": "Send an important email", "approval": ""}, config=config
)


# Step 11: Display Human Approval Request
print("\n===== HUMAN APPROVAL REQUEST =====")

print(result["__interrupt__"][0].value)


# Step 12: Get Human Decision
user_decision = input("\nApprove this action? (yes/no): ").strip().lower()


# Step 13: Resume Graph
final_result = graph.invoke(Command(resume=user_decision), config=config)


# Step 14: Display Final Result
print("\n===== FINAL RESULT =====")
print(final_result["approval"])


# This example uses an in-memory checkpoint.
# For persistent production workflows,
# configure a durable checkpointer and manage thread identities securely.
