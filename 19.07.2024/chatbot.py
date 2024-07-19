def chatbot():
    responses = {
        "hello": "Hi there! How can I help you today?",
        "hi": "Hello! How can I assist you?",
        "how are you": "I'm just a program, but I'm doing great! How about you?",
        "bye": "Goodbye! Have a great day!",
        "thank you": "You're welcome! If you have any other questions, feel free to ask.",
        "help": "Sure, I'm here to help. What do you need assistance with?",
        "what is your name": "I am a simple chatbot created to assist you."
    }
    
    print("Welcome to the chatbot! Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ").lower()
        if user_input == 'exit':
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = responses.get(user_input, "I'm sorry, I don't understand that.")
        print(f"Chatbot: {response}")
chatbot()
