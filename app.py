import os
from typing import List, Tuple

import gradio as gr
from huggingface_hub import InferenceClient


HF_TOKEN = os.getenv("HF_API_TOKEN")
MODEL_ID = os.getenv("HF_MODEL_ID", "mistralai/Mixtral-8x7B-Instruct-v0.1")


def build_client() -> InferenceClient | None:
    """
    Create a Hugging Face InferenceClient if HF_API_TOKEN is available.
    """
    if not HF_TOKEN:
        return None
    return InferenceClient(model=MODEL_ID, token=HF_TOKEN)


client = build_client()


def format_messages(message: str, history: List[Tuple[str, str]]) -> List[dict]:
    """
    Convert Gradio chat history into OpenAI-style chat messages.
    """
    messages: List[dict] = [
        {
            "role": "system",
            "content": (
                "You are a helpful AI assistant. "
                "Give clear, concise answers and explain concepts simply."
            ),
        }
    ]

    for human, bot in history:
        if human:
            messages.append({"role": "user", "content": human})
        if bot:
            messages.append({"role": "assistant", "content": bot})

    messages.append({"role": "user", "content": message})
    return messages


def chat_bot(message: str, history: List[Tuple[str, str]]) -> str:
    """
    Main chat function used by Gradio.
    """
    if client is None:
        return (
            "HF_API_TOKEN environment variable is not set.\n\n"
            "1. Go to Hugging Face and create a personal access token.\n"
            "2. Set it locally, for example:\n"
            "   - On Windows (PowerShell):  $env:HF_API_TOKEN = 'your_token_here'\n"
            "   - In a .env file: HF_API_TOKEN=your_token_here\n"
            "3. Restart the app.\n\n"
            "Once HF_API_TOKEN is set, the app will call the Hugging Face Inference API."
        )

    messages = format_messages(message, history)

    try:
        completion = client.chat_completion(
            model=MODEL_ID,
            messages=messages,
            max_tokens=256,
            temperature=0.7,
        )
        # huggingface_hub returns a structure similar to OpenAI
        return completion.choices[0].message["content"]
    except Exception as e:
        return f"Error while calling Hugging Face Inference API: {e}"


demo = gr.ChatInterface(
    fn=chat_bot,
    title="Build Your Own GenAI Model – Chatbot",
    description=(
        "A simple GenAI chatbot built with Python, Gradio, and the "
        "Hugging Face Inference API. Configure your HF_API_TOKEN and HF_MODEL_ID "
        "to experiment with different models."
    ),
)


if __name__ == "__main__":
    port = int(os.getenv("PORT", "7860"))
    demo.launch(server_name="0.0.0.0", server_port=port)

