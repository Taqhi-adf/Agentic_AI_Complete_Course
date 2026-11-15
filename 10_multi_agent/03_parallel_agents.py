### Code 29: Parallel agents

# Create `10_multi_agent/03_parallel_agents.py`.

from concurrent.futures import ThreadPoolExecutor
from langchain_ollama import ChatOllama

# Initialize local LLM
llm = ChatOllama(model="llama3.2:3b")


# Define an agent
def run_agent(role, task):

    prompt = f"""
    You are a {role}.

    Complete this task:
    {task}

    Give a clear and detailed explanation.
    """

    # Execute LLM inside the function
    response = llm.invoke(prompt).content

    # Return role and response
    return role, response


# Common task
task = "Explain Agentic AI applications"

# Two agents
roles = ["researcher", "analyst"]


# Execute agents in parallel
with ThreadPoolExecutor(max_workers=2) as executor:
    futures = [executor.submit(run_agent, role, task) for role in roles]

    for future in futures:
        role, result = future.result()

        print("\n==========", role.upper(), "==========")
        print(result)

# With an 8 GB RAM machine,
# begin with one local LLM request at a time.
# Parallel inference can increase memory usage significantly.
