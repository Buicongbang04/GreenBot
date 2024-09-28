# Import libraries
from g4f.client import Client
import gradio as gr
import warnings
warnings.filterwarnings("ignore")

# Init G4F Client
client = Client()

# Defined the chatbot response
def get_response(prompt):
    response = client.chat.completions.create(
        model='gpt-4-turbo',
        messages=[
            {'role': 'user', 'content': prompt},
        ],
    )
    return response.choices[0].message.content

# Gradio user interface
interface = gr.Interface(
    fn=get_response,
    inputs=gr.Textbox(
        lines=2,
        placeholder="What thing do you want to ask..."
    ),
    outputs='text',
    title="GreenBot AI",
    description="I'm here to help you with your plant! Feel free to ask your own.",
)

if __name__ == "__main__":
    interface.launch()