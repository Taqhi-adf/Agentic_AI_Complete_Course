### Code 12: Reflection agent

# An agent reviews its own output and attempts to improve it.

# Create `06_agent_planning/02_reflection_agent.py`.


import ollama


def ask_llm(prompt):
    result = ollama.chat(
        model="llama3.2:3b", messages=[{"role": "user", "content": prompt}]
    )
    return result["message"]["content"]


task = "give all generative and agentic ai companies with there websites in hyderabad to apply for genai jobs."
draft = ask_llm(task)
review = ask_llm("Review this answer and identify mistakes:\n" + draft)
improved = ask_llm(
    "Improve this answer using the review:\n" + review + "\nOriginal answer:\n" + draft
)
print("Original:")
print(draft)
print("\nReview:")
print(review)
print("\nImproved:")
print(improved)
