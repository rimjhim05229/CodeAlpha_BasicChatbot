[README.md](https://github.com/user-attachments/files/35339879/README.md)
# Basic Chatbot – CodeAlpha Python Programming Internship (Task 4)

A simple rule-based chatbot built with Python. It accepts messages from the user and responds using predefined replies.

## Features
- Responds to greetings such as `hello`, `hi`, and `hey`.
- Replies to `how are you` and `what is your name`.
- Shows a helpful default response for unknown messages.
- Continues chatting until the user types `bye`, `exit`, or `quit`.
- Uses separate Python modules for the chat logic and predefined responses.

## Project Structure

```text
CodeAlpha_BasicChatbot/
├── main.py
├── chatbot/
│   ├── __init__.py
│   ├── bot.py
│   └── responses.py
├── README.md
└── .gitignore
```

## Requirements
- Python 3 installed
- No external libraries required

## How to Run
1. Open this project folder in VS Code.
2. Open the terminal in VS Code.
3. Run:

```bash
python main.py
```

## Example

```text
Welcome to CodeAlpha Chatbot
You: hello
Bot: Hi! Nice to meet you.

You: how are you
Bot: I'm fine, thanks! How are you?

You: bye
Bot: Goodbye! Have a great day!
```

## Concepts Used
- Functions
- Dictionaries
- Strings and string methods
- `while` loop
- `if-else` conditions
- User input and output

Created as Task 4 of the CodeAlpha Python Programming Internship.
