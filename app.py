import os
from typing import Optional

import gradio as gr
import torch
from diffusers import StableDiffusionPipeline


HF_TOKEN = os.getenv("HF_API_TOKEN")
MODEL_ID = os.getenv("HF_MODEL_ID", "runwayml/stable-diffusion-v1-5")


def load_pipeline() -> StableDiffusionPipeline:
    """
    Load a Stable Diffusion pipeline similar to the base model download
    in the original NxtWave notebook.
    """
    device = "cuda" if torch.cuda.is_available() else "cpu"
    dtype = torch.float16 if device == "cuda" else torch.float32

    auth_token: Optional[str] = HF_TOKEN if HF_TOKEN else None

    pipe = StableDiffusionPipeline.from_pretrained(
        MODEL_ID,
        torch_dtype=dtype,
        use_auth_token=auth_token,
        safety_checker=None,
    )
    pipe.to(device)
    return pipe


pipe = load_pipeline()


def generate_image(
    prompt: str,
    guidance_scale: float = 7.5,
    num_inference_steps: int = 30,
    seed: int = 42,
):
    """
    Text-to-image generation using Stable Diffusion.
    """
    if not prompt.strip():
        return None

    device = pipe.device
    generator = torch.Generator(device=device)
    if seed is not None:
        try:
            generator = generator.manual_seed(int(seed))
        except ValueError:
            generator = generator.manual_seed(42)

    with torch.autocast(device.type if device.type != "mps" else "cpu"):
        image = pipe(
            prompt=prompt,
            guidance_scale=guidance_scale,
            num_inference_steps=num_inference_steps,
            generator=generator,
        ).images[0]

    return image


demo = gr.Interface(
    fn=generate_image,
    inputs=[
        gr.Textbox(label="Prompt", lines=2, placeholder="A photo of a futuristic city at sunset"),
        gr.Slider(1.0, 15.0, value=7.5, step=0.5, label="Guidance scale"),
        gr.Slider(5, 50, value=30, step=1, label="Inference steps"),
        gr.Number(value=42, label="Seed (optional, integer)"),
    ],
    outputs=gr.Image(label="Generated image"),
    title="Build Your Own GenAI Model – Stable Diffusion Image Generator",
    description=(
        "Local Stable Diffusion text-to-image app inspired by the NxtWave "
        "Fast-Dreambooth notebook. Uses a Hugging Face model like "
        "`runwayml/stable-diffusion-v1-5`."
    ),
)


if __name__ == "__main__":
    port = int(os.getenv("PORT", "7860"))
    demo.launch(server_name="0.0.0.0", server_port=port)

