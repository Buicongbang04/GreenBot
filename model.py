import openai
from torch.backends.quantized import engine

# Cấu hình API key
# openai.api_key = "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"

# Model's response
messages = [
    {"role": "system", "content": "You are a kindly and helpful assistant!"},
]

def get_response(prompt):
    messages.append({"role": "user", "content": prompt})
    chat = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages,
    )

    return chat.choices[0].messages.content

def chatbot():
    print("Welcome to chatbot")
    while True:
        user_input = input("Customer: ")
        if user_input.lower().strip() == "quit":
            print("Thank you for using chatbot")
            break

        response = get_response(user_input)
        print(f"Bot: {response}")
        messages.append({"role": "system", "content": response})

chatbot()
