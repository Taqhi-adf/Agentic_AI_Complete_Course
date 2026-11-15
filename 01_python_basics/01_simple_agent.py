# Level 1 – Python fundamentals for agents
# First learn how an agent receives information, processes it, and produces an action.

### Code 1: Simple AI agent


def agent(user_input):
    if "hello" in user_input.lower():
        return "Hello! How can I help you?"
    elif "weather" in user_input.lower():
        return "I can help you check weather information."
    elif "python" in user_input.lower():
        return "Python is used to build AI agents."
    else:
        return "I don't know that yet."

    while True:
        question = input("You: ")
        if question.lower() == "exit":
            print("Agent: Goodbye!")
            break
        response = agent(question)
        print("Agent:", response)
