# Define the bot's responses
bot_responses = {
    "greeting": "Hello! How can I assist you today?",
    "farewell": "Goodbye! Have a great day!",
    "ask_time": "I'm sorry, I cannot provide the current time.",
    "ask_date": "I'm sorry, I cannot provide today's date.",
    "weather": "I'm unable to provide weather updates at the moment.",
    "joke": "Why don't scientists trust atoms? Because they make up everything!",
    "quote": "Here's a quote for you: 'The only way to do great work is to love what you do.' - Steve Jobs",
    "help": "I'm here to assist you. You can ask me about the weather, time, date, or even for a joke or quote.",
    "thank_you": "You're welcome! If you have any other questions, feel free to ask.",
    "unknown": "I'm sorry, I didn't understand that. Can you please rephrase?"
}

# Function to get the bot's response
def get_bot_response(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()
    # Iterate over the intents and check if any keyword is in the user input
    for intent, response in bot_responses.items():
        if intent in user_input:
            return response
    # If no intent matches, return the 'unknown' response
    return bot_responses["unknown"]

# Main loop for continuous interaction
print("Bot: Hi there! Type 'quit' to end the chat.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ['quit', 'exit']:
        print("Bot: Goodbye!")
        break
    print(f"Bot: {get_bot_response(user_input)}")
