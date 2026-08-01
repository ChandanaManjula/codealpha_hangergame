def get_bot_response(user_message):
    message = user_message.lower().strip()
    
    if "hello" in message or "hi" in message:
        return "Hello! How can I help you today?"
        
    elif "your name" in message or "who are you" in message:
        return "I am PyBot, a simple rule-based chatbot built in Python!"
        
    elif "how are you" in message:
        return "I am doing great, thank you! How are you doing?"
        
    elif "help" in message:
        return "You can ask me about my name, how I am doing, or say 'bye' to exit."
        
    else:
        return "I am sorry, I do not understand that yet. Type 'help' for things you can ask me."

def start_chatbot():
    print("=========================================")
    print("🤖 Welcome to PyBot! Type 'bye' to exit.")
    print("=========================================")
    
    while True:
        user_input = input("\nYou: ")
        
        if user_input.lower().strip() == "bye":
            print("PyBot: Goodbye! Have a great day!")
            break  
            
        response = get_bot_response(user_input)
        
        print(f"PyBot: {response}")

if __name__ == "__main__":
    start_chatbot()
