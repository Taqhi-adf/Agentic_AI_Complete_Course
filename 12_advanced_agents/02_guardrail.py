### Code 33: Input guardrail

# Create `12_advanced_agents/02_guardrail.py`.


def validate_input(question):
    if not question.strip():
        return False
    if len(question) > 1000:
        return False
    blocked_words = ["delete all files", "steal passwords"]
    if any(word in question.lower() for word in blocked_words):
        return False
    return True


question = input("Enter your request: ")
if validate_input(question):
    print("Input accepted")
else:
    print("Input rejected")


# This is only a basic validation example,
# not a complete security system.
# Real guardrails also require authorization checks,
# tool-level restrictions,
# output validation,
# and audit logging.
