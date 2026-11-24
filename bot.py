"""Chat loop for the basic rule-based chatbot."""

from chatbot.responses import RESPONSES, DEFAULT_RESPONSE


def get_response(user_message):
    """Return a predefined response for the user's message."""
    message = user_message.strip().lower()
    return RESPONSES.get(message, DEFAULT_RESPONSE)


def start_chat():
    """Start the chatbot and continue until the user exits."""
    print("=" * 45)
    print("        Welcome to CodeAlpha Chatbot")
    print("=" * 45)
    print("Type 'hello', 'how are you', or 'bye' to exit.\n")

    while True:
        user_message = input("You: ").strip()

        if not user_message:
            print("Bot: Please type something.\n")
            continue

        response = get_response(user_message)
        print(f"Bot: {response}\n")

        if user_message.lower() in ("bye", "exit", "quit"):
            break
