# Build Your Own GenAI Model – Learning Notes

This project recreates the **NxtWave “Build your own GenAI Model”** hands‑on session, but in a clean Python/Jupyter‑friendly format that you can run locally and also deploy to **Hugging Face Spaces** and **Render**.

---

## 1. Project Setup (Local)

1. **Create virtual environment (recommended)**
   - On Windows (PowerShell):
     - `python -m venv venv`
     - `.\venv\Scripts\activate`

2. **Install dependencies**
   - From the project folder:
     - `pip install -r requirements.txt`

3. **Set environment variables**
   - Get a **Hugging Face access token** from your HF profile (with “read” permission).
   - Set token (examples):
     - PowerShell (current session):  
       ` $env:HF_API_TOKEN = "your_token_here" `
   - Optional: choose a different model (default is `mistralai/Mixtral-8x7B-Instruct-v0.1`):  
     - ` $env:HF_MODEL_ID = "your_model_id"` (for example a smaller instruct model).

4. **Run the app locally**
   - `python app.py`
   - Open the URL shown in the terminal (usually `http://127.0.0.1:7860`).

You can also open the project in **Jupyter / VSCode / JupyterLab** and import functions from `app.py` if you want to experiment inside a notebook.

---

## 2. Understanding the Code (`app.py`)

- **Libraries**
  - `huggingface_hub.InferenceClient`: calls Hugging Face Inference API (hosted models).
  - `gradio`: creates a simple web UI/chat interface.

- **Key parts**
  - `HF_API_TOKEN` and `HF_MODEL_ID` are read from environment variables.
  - `build_client()` creates an `InferenceClient` only when the token is available.
  - `format_messages()` converts chat history into a list of messages with roles (`system`, `user`, `assistant`).
  - `chat_bot()`:
    - Builds the full conversation history.
    - Sends it to `client.chat_completion(...)`.
    - Returns the generated answer.
  - `demo = gr.ChatInterface(...)` defines the UI.
  - `demo.launch(server_name="0.0.0.0", server_port=PORT)` runs the web server (works locally and on cloud platforms).

Try reading `app.py` from top to bottom and write your own explanation in this file below these notes.

---

## 3. Deploying to Hugging Face Spaces (high level)

1. Create a new **Space** on Hugging Face (type: **Gradio**).
2. Push these files to the Space repository:
   - `app.py`
   - `requirements.txt`
   - (optional) `NOTES.md`, `.gitignore`
3. In the Space settings, add a **secret** called `HF_API_TOKEN` with your token value.
4. The Space should automatically build and run; you will see the Gradio UI.

You can come back here and write detailed step‑by‑step notes once you deploy for the first time.

---

## 4. Deploying to Render (high level)

1. Push this project to **GitHub**.
2. On Render:
   - Create a new **Web Service** from your GitHub repo.
   - Set **Build Command**: `pip install -r requirements.txt`
   - Set **Start Command**: `python app.py`
3. In the **Environment** section, add:
   - `HF_API_TOKEN` = your token
   - (optional) `HF_MODEL_ID` = your preferred model
4. Render will set `PORT` automatically; our `app.py` already reads it.

Again, after you deploy once, add your own step‑by‑step notes here in this file.

---

## 5. Your Practice Ideas

Use this section like a mini diary for your learning. Example ideas:

- Change the system prompt to make the bot:
  - a **coding tutor**
  - an **English speaking partner**
  - a **math problem solver**
- Try different models by changing `HF_MODEL_ID`.
- Add input limits or extra buttons in the Gradio UI.

Write your own bullets and experiments below:

- [ ] Experiment 1:
- [ ] Experiment 2:
- [ ] Experiment 3:

