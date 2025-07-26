import re

def get_response(message):
    message = message.lower()

    # Greeting
    if re.search(r'\b(hi|hello|hey)\b', message):
        return "Hi there! How can I help you?"

    # Identity question
    elif re.search(r'\b(who are you|what is your name)\b', message):
        return "I'm a basic chatbot created to chat with you."

    # Help request
    elif re.search(r'\b(help|assist|support)\b', message):
        return "Sure, I'm here to help. What do you need?"

    # Goodbye
    elif re.search(r'\b(bye|goodbye|see you)\b', message):
        return "Bye! Have a nice day."

    # Default
    else:
        return "Sorry, I didn't get that. Can you say it differently?"

def chat():
    print("Chatbot: Hello! Type something to start chatting (type 'bye' to quit).")
    while True:
        user = input("You: ")
        reply = get_response(user)
        print("Chatbot:", reply)
        if re.search(r'\b(bye|goodbye|see you)\b', user.lower()):
            break

if __name__ == '__main__':
    chat()