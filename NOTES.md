# Build Your Own GenAI Model – Stable Diffusion Notes

This project follows the spirit of the **NxtWave “Build your own GenAI Model”** notebook you have (`Fast-Dreambooth` / Stable Diffusion), but rebuilt to run locally on your machine (Python / Jupyter) and to deploy on **Hugging Face Spaces** and **Render**.

The original Colab notebook:
- Mounted Google Drive
- Installed many system-level dependencies
- Downloaded **Stable Diffusion 1.5 / 2.1** from Hugging Face
- Trained / fine-tuned with Dreambooth
- Exposed a Gradio interface for text‑to‑image

Here we focus on a clean, minimal **text‑to‑image app** using Stable Diffusion.

---

## 1. Project Setup (Local, Windows)

1. **Create virtual environment (recommended)**
   - PowerShell:
     - `python -m venv venv`
     - `.\venv\Scripts\activate`

2. **Install dependencies**
   - From the project folder:
     - `pip install -r requirements.txt`

3. **Hugging Face token & model**
   - Create a token on Hugging Face (profile → Access Tokens, with “read” permission).
   - In PowerShell (for current session):
     - ` $env:HF_API_TOKEN = "your_token_here" `
   - Optional: change the model (default is `runwayml/stable-diffusion-v1-5`):
     - ` $env:HF_MODEL_ID = "your-model-id"`  
       (e.g. a smaller SD model or your own fine‑tuned one uploaded to HF).

4. **Run the app locally**
   - `python app.py`
   - Open the URL shown in the terminal (usually `http://127.0.0.1:7860`).
   - On first run, the model weights will download from Hugging Face (this can be several GB and take time).

You can also open this folder in **Jupyter / VSCode** and call `generate_image` from a notebook for experiments.

---

## 2. Understanding the Code (`app.py`)

- **Libraries**
  - `torch`: tensor + GPU/CPU computing.
  - `diffusers.StableDiffusionPipeline`: loads Stable Diffusion for text‑to‑image.
  - `gradio`: simple web UI.

- **Key parts**
  - `HF_API_TOKEN` and `HF_MODEL_ID` are read from environment variables.
  - `load_pipeline()`:
    - Chooses `cuda` if GPU is available, otherwise `cpu`.
    - Downloads / loads the Stable Diffusion model from Hugging Face.
  - `generate_image()`:
    - Takes `prompt`, `guidance_scale`, `num_inference_steps`, and `seed`.
    - Runs the pipeline and returns one generated image.
  - `demo = gr.Interface(...)`:
    - Builds a small UI similar to the Gradio part of your Colab notebook.
  - `demo.launch(server_name="0.0.0.0", server_port=PORT)`:
    - Runs a web server that works locally and on cloud (HF Spaces, Render).

Try reading `app.py` from top to bottom and write your own one‑paragraph explanation below these notes.

---

## 3. Deploying to Hugging Face Spaces

1. **First push to GitHub** (already set up for your repo).
2. On Hugging Face:
   - Create a new **Space** (type: **Gradio**).
   - Connect it to your GitHub repo (or copy these files into the Space repo):
     - `app.py`
     - `requirements.txt`
     - (optional) `NOTES.md`, `.gitignore`
3. In the Space **Settings → Variables and secrets**:
   - Add `HF_API_TOKEN` with your HF token.
   - Optional: `HF_MODEL_ID` with the exact model you want to use.
4. Save the settings; the Space will build and run automatically.
5. When build is green, open the Space URL and test prompts.

After your first deployment, come back here and add your own “HF Spaces deployment steps” in your own words.

---

## 4. Deploying to Render

1. Make sure your latest code is **pushed to GitHub**.
2. On Render:
   - Create **New → Web Service** from your GitHub repo.
   - Set **Environment** = Python 3.x.
   - Set **Build Command**:  
     `pip install -r requirements.txt`
   - Set **Start Command**:  
     `python app.py`
3. In Render **Environment Variables**:
   - `HF_API_TOKEN` = your HF token
   - Optional `HF_MODEL_ID` = your chosen model id
4. Deploy; Render sets `PORT` automatically (our app reads it).

Write down any issues you hit during Render deploy and how you fixed them here for future reference.

---

## 5. Your Practice Ideas

Use this like a mini notebook for experiments, similar to trying different settings in the original NxtWave notebook.

- Change the **prompt style** (photorealistic, anime, pixel art, logo design, etc.).
- Change **guidance scale** and **steps** to see effect on quality / speed.
- Try a different `HF_MODEL_ID` (e.g. a fine‑tuned SD model from Hugging Face).
- Later: we can add training / fine‑tuning steps inspired by the Dreambooth section.

Write your own bullets and experiments below:

- [ ] Experiment 1:
- [ ] Experiment 2:
- [ ] Experiment 3:

