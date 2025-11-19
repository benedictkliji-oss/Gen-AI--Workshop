import gradio as gr
from groq import Groq

# Initialize Groq client
client = Groq(api_key="API Code")   # <-- Replace with your key

# System prompt
def initialize_messages():
    return [
        {
            "role": "system",
            "content": """You are a highly skilled motorcycle mechanic
with years of hands-on experience in diagnosing, repairing, and
troubleshooting motorcycles of all brands.

Your job is to:
1. Analyse symptoms.
2. Ask relevant questions.
3. Identify causes.
4. Provide step-by-step troubleshooting.
5. Suggest repairs & safety steps.
6. Explain concepts simply.

Always answer professionally. Never suggest unsafe practices."""
        }
    ]

messages_prmt = initialize_messages()

# Chatbot logic
def customLLMBot(user_input, history):
    global messages_prmt

    messages_prmt.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        messages=messages_prmt,
        model="llama-3.3-70b-versatile",
    )

    LLM_reply = response.choices[0].message.content
    messages_prmt.append({"role": "assistant", "content": LLM_reply})

    return LLM_reply


# 🟢 Gradio Interface
iface = gr.ChatInterface(
    fn=customLLMBot,
    chatbot=gr.Chatbot(height=350),
    textbox=gr.Textbox(placeholder="Describe your motorcycle issue..."),
    title="Motorcycle Mechanic Chatbot",
    description="AI-based mechanic assistant using Groq LLaMA 3.3 model",
    theme="soft",
    examples=[
        "Engine not starting in cold morning",
        "Bike giving low mileage",
        "Metallic noise from engine",
        "Throttle response is slow"
    ]
)

# Run locally
iface.launch(share=False)   # Set share=True if you want a public link
