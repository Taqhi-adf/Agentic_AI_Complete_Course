# Level 9 – Multi-agent systems

# Advanced engineering
# A multi-agent system uses multiple specialized agents that cooperate.

# [🧠 Building a Supervisor Multi-Agent System with LangGraph Hierarchical Intelligence in Action | by Mani | Medium](https://images.openai.com/static-rsc-4/iYcOIrXkFMkCMrqXHLKpGwzmelKWPUBXIhj9U2-L7vcAd4j_kyNOEn8uAZOqDlf2HwqE7t-vzR8I3YIwpEAWmlBbMKFU3VpWkUY1SFK4wnTEgyQcGSybKCocVRuUIsTNwYzvlBa-xBUJ-ubXg8QnDH1PGPpqFOSGKOOwQquvQAY?purpose=inline)

# [medium.com](https://medium.com/%40mnai0377/building-a-supervisor-multi-agent-system-with-langgraph-hierarchical-intelligence-in-action-3e9765af181c?utm_source=chatgpt.com)

# Learn these architectures:
# 1. Supervisor agent.
# 2. Hierarchical agents.
# 3. Sequential agents.
# 4. Parallel agents.
# 5. Collaborative agents.
# 6. Debate agents.
# 7. Researcher and writer agents.
# 8. Planner and executor agents.
# 9. Reviewer and coder agents.
# 10. Swarm-style handoffs.

### Code 27: Build a two-agent system

# Create `10_multi_agent/01_two_agents.py`.

# 01_two_agents.py

from langchain_ollama import ChatOllama

# Initialize LLM
llm = ChatOllama(model="llama3.2:3b", temperature=0.3)


# AGENT 1: RESEARCHER
def researcher(topic):

    research_prompt = f"""
    You are an expert research agent.

    Research the following topic:
    {topic}

    Explain:
    1. What is it?
    2. Why is it important?
    3. How does it work?
    4. Real-world applications.

    Provide clear and accurate information.
    """

    response = llm.invoke(research_prompt)

    return response.content


# AGENT 2: WRITER
def writer(research):

    writer_prompt = f"""
    You are a professional technical writer.

    Create a well-structured article using
    the following research:

    {research}

    Include:
    1. Title
    2. Introduction
    3. Main explanation
    4. Real-world examples
    5. Conclusion.
    """

    response = llm.invoke(writer_prompt)

    return response.content


# MAIN WORKFLOW

topic = "Agentic AI"

# First agent researches
research = researcher(topic)

# Second agent writes using research
article = writer(research)


# DISPLAY RESULTS

print("\n========== RESEARCH AGENT OUTPUT ==========")
print(research)

print("\n========== WRITER AGENT OUTPUT ==========")
print(article)
