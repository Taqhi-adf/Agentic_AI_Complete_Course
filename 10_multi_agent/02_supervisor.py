### Code 28: Supervisor agent

# Create `10_multi_agent/02_supervisor.py`.


from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2:3b")


def researcher(task):
    return "Research completed for: " + task


def coder(task):
    return "Code generation requested for: " + task


def analyst(task):
    return "Analysis completed for: " + task


def supervisor(task):
    prompt = f"""Choose one specialist for this task.
    Available specialists:
    researcher    coder    analyst    Task: {task}    
    Return only the specialist name."""
    response = llm.invoke(prompt)
    choice = response.content.strip().lower()
    print(choice)


# This is a simplified supervisor demonstration.
# For a production implementation,
# validate the model's routing response using structured output and use real specialist agents.
