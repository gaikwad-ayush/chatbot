import random
import time

# Simulated typing delay for bot replies
def bot_print(message):
    time.sleep(0.6)
    print(f"ChatBot: {message}")

# Multiple fun replies for variety
responses = {
    "hi": ["Hey there!", "Hi! Nice to see you.", "Hello! What's up?"],
    "hello": ["Hello! How can I make your day better?", "Hi! Ready to chat?", "Hello, human!"],
    "how are you": ["I'm doing great! Thanks for asking.", "All systems running smoothly.", "Feeling chatty today!"],
    "help": ["Try asking about the weather, time, or just say something fun.", "Need help? Just type something like 'what can you do'.", "I'm simple, but I can chat all day!"],
    "who are you": ["I'm a terminal-based chatbot made in Python.", "Just a little program trying to sound clever."],
    "your name": ["I go by TermiBot.", "You can call me whatever you like — but I prefer TermiBot."],
    "what can you do": ["I can chat, tell jokes, and pretend I'm smart.", "Mostly I just talk, but I do it well!"],
    "thanks": ["You're welcome!", "Anytime.", "Glad to help!"],
    "joke": [
        "Why don’t robots panic? Because they have nerves of steel.",
        "Why was the computer cold? It left its Windows open.",
        "I told my bot friend a joke… now it won't stop laughing in binary."
    ],
    "bye": ["Goodbye! Take care.", "See you next time.", "Chat later!"]
}

# Start chat
bot_print("Hi there! I'm TermiBot. Type 'bye' to end the conversation.")

while True:
    user_input = input("You: ").lower().strip()

    if user_input == "bye":
        bot_print(random.choice(responses["bye"]))
        break
    elif user_input in responses:
        bot_print(random.choice(responses[user_input]))
    else:
        bot_print("Hmm, I didn’t quite get that. Try something like 'hi', 'joke', or 'help'.")
