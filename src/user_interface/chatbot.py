import openai
from GPT_NeoXT_Chat_Base_20B import GPTNeoXTChatBase20B


class Chatbot:
    def __init__(self):
        self.model = GPTNeoXTChatBase20B()

    def generate_response(self, user_input):
        prompt = f"{user_input}"
        response = self.model.generate(prompt)
        return response.strip()


if __name__ == "__main__":
    chatbot = Chatbot()

    print("Welcome to the Generative AI Descriptor chatbot!")
    print("You can ask questions or request descriptions for various media types.")
    print("Type 'quit' to exit the chatbot.")

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == "quit":
            break

        response = chatbot.generate_response(user_input)
        print(f"Chatbot: {response}")
