# AI Portrait & Avatar Generator

Generate portraits and avatars from text prompts using **Stable Diffusion**. Built with Python, Gradio, and Hugging Face diffusers.

## Quick Start

```bash
pip install -r requirements.txt
$env:HF_API_TOKEN = "your_huggingface_token"   # PowerShell
python app.py
```

Open **http://127.0.0.1:7860** in your browser.

## Tech Stack

- Python, PyTorch, Hugging Face diffusers
- Stable Diffusion (runwayml/stable-diffusion-v1-5)
- Gradio (web UI)

## Deploy

- **Hugging Face Spaces** — Gradio SDK, add `HF_API_TOKEN` secret
- **Render** — Web Service, Build: `pip install -r requirements.txt`, Start: `python app.py`

See `PLAN.md` for the full project plan and `NOTES.md` for detailed setup.
