# chatbot_terminal.py

print("ChatBot: Hello! I'm your terminal chatbot. Type 'bye' to exit.")

# Rule-based response dictionary
responses = {
    "hi": "Hello! How can I help you?",
    "hello": "Hi there! Need any help?",
    "how are you": "I'm just a bunch of code, but I'm doing fine!",
    "help": "You can ask me about weather, time, or just say hi!",
    "bye": "Goodbye! Have a great day!",
    "who are you": "I'm a simple chatbot built using Python.",
    "thanks": "You're welcome!",
    "what can you do": "I can respond to basic messages like greetings and FAQs.",
    "your name": "I’m TerminalBot!"
}

# Start conversation loop
while True:
    user_input = input("You: ").lower()

    if user_input == "bye":
        print("ChatBot: Goodbye! ")
        break

    # Get response or default
    response = responses.get(user_input, " ChatBot: I didn’t understand that. Try something else.")
    print(f" ChatBot: {response}")
