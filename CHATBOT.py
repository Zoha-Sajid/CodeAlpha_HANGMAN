"""
This is a simple AI-powered chatbot program built using Python's Tkinter for the GUI and spaCy for Natural Language Processing (NLP). The chatbot can respond to various inputs, such as greetings, questions about itself, jokes, and general inquiries like the weather.

### Features:
1. **Greeting Responses**: The bot recognizes common greetings and responds with a friendly message.
2. **Jokes**: The bot can tell jokes when asked.
3. **Questions about the bot**: If asked about the bot's name or identity, it will provide a response describing itself.
4. **Weather and General Information**: If the user asks about the weather, the bot will inform them that it cannot check the weather but invites further conversation.
5. **Entity Recognition**: The bot uses spaCy's NLP capabilities to recognize names and refer to the user by their name if mentioned.
6. **Scrollable Chat Interface**: The GUI includes a scrollable chat area where the conversation history is displayed, and a text input area for user interaction.
7. **User Interaction**: The user can send messages to the bot, and the bot will respond intelligently based on the user input.

### Game Flow:
1. **Greeting**: The bot greets the user and prompts for their input.
2. **User Input**: The user types a message, and the bot processes the input using spaCy for better understanding.
3. **Bot Response**: Based on the input, the bot generates an appropriate response, such as a greeting, joke, or a general response.
4. **Conversation History**: The chat area is updated with both the user's message and the bot's response.
5. **Entity Recognition**: If the user mentions a name, the bot will acknowledge the name in its response.
"""

import tkinter as tk
from tkinter import scrolledtext
import spacy
import random

# Load spaCy's small English model for NLP
nlp = spacy.load("en_core_web_sm")

# Define a list of possible responses to make the bot smarter
greetings = ["Hello! How can I assist you today?", "Hi there! What can I do for you?", "Hey! Need help?"]
jokes = [
    "Why don't skeletons fight each other? They don't have the guts!",
    "What do you call fake spaghetti? An impasta!",
    "Why can't you give Elsa a balloon? Because she will let it go!"
]
questions_about_bot = [
    "I am a friendly chatbot created to chat with you. What can I help you with?",
    "I'm a bot, your assistant. How can I assist today?"
]

# Function to generate intelligent responses based on user input
def generate_response(user_input):
    doc = nlp(user_input.lower())  # Process user input with spaCy

    # Greeting response
    if any(greeting in user_input.lower() for greeting in ["hello", "hi", "hey", "howdy", "morning", "evening"]):
        return random.choice(greetings)

    # Questions about the bot itself
    if "your name" in user_input.lower() or "who are you" in user_input.lower():
        return random.choice(questions_about_bot)

    # Check for jokes
    if "joke" in user_input.lower():
        return random.choice(jokes)

    # Handle asking about the weather or general information
    if "weather" in user_input.lower():
        return "I can't check the weather for you, but I can chat about other things! Ask me something else."

    # Entity recognition for names (PERSON)
    person_entities = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
    if person_entities:
        return f"Nice to meet you, {', '.join(person_entities)}! How can I help you?"

    # Handle default unknown input
    return "Hmm... I couldn't understand that. Can you ask something else?"

# Function to handle sending and displaying messages
def send_message():
    user_input = entry.get()  # Get the user's input
    if user_input:
        # Display the user's message in the chat area
        text_area.insert(tk.END, "You: " + user_input + "\n")
        entry.delete(0, tk.END)  # Clear the input field

        # Generate a response from the chatbot
        response = generate_response(user_input)

        # Display the bot's response in the chat area
        text_area.insert(tk.END, "Bot: " + response + "\n")

        # Auto-scroll to the bottom of the chat area
        text_area.yview(tk.END)

# Set up the graphical user interface (GUI)
root = tk.Tk()
root.title("Smart Chatbot")
root.geometry("400x500")
root.configure(bg="#f9f9f9")

# Create a scrollable text area for the conversation history
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, font=("Arial", 12), bg="#fff", fg="#333")
text_area.pack(pady=10)
text_area.insert(tk.END, "Bot: Hello! I'm here to chat with you. Type something!\n")

# Create an input field for the user to type their messages
entry = tk.Entry(root, font=("Arial", 12), width=40)
entry.pack(pady=5)

# Create a send button to submit the user's message
send_button = tk.Button(root, text="Send", font=("Arial", 12), bg="#4CAF50", fg="white", command=send_message)
send_button.pack(pady=10)

# Start the main GUI loop
root.mainloop()
