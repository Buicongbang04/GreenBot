from g4f.client import Client
import warnings
warnings.filterwarnings("ignore")

client = Client()

def get_response(prompt):
    response = client.chat.completions.create(
        model = 'gpt-3.5-turbo',
        messages = [
            {'role': 'user',
             'content': prompt}
        ]
    )

    return response.choices[0].message.content

def chatbot():
    print("Welcome to chatbot")
    while True:
        user_input = input("Customer: ")
        if user_input.lower().strip() == "quit":
            print("Thank you for using chatbot")
            break

        response = get_response(user_input)
        print(f"Bot: {response}")


chatbot()
