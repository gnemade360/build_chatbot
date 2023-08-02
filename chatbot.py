def get_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hello! How can I assist you?"

    elif "how are you" in user_input:
        return "I'm just a chatbot, but thanks for asking!"

    elif "goodbye" in user_input:
        return "Goodbye! Have a great day."

    else:
        return "I'm sorry, I don't understand. Can you please rephrase your question?"

def main():
    print("Chatbot: Hi! I'm your friendly chatbot. Type 'Goodbye' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "goodbye":
            print("Chatbot: Goodbye! Have a great day.")
            break

        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
