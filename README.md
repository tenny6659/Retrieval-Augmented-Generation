Code-Conversion-Pipeline-using-LLMs
SAS to Python Converter using Ollama ---- A tool that converts .sas files to clean .py files using LLaMA 3 via Ollama. Supports multiple uploads, automated folder watching, and a simple Streamlit UI.

📁 Structure
config/ → Loads .env (model config)
data/input/ → Drop .sas files here
data/output/ → Output .py files (timestamped)
models/ → Pydantic input/output schemas
prompts/ → Template prompt for LLM
src/components/ → File handling, conversion logic
app/ → Streamlit UI
scripts/ → Auto-watch for SAS files
api/ → Optional FastAPI routes
🚀 Usage
Install dependencies

pip install -r requirements.txt
Pull the model
Pull the model ollama pull llama3

Run the Streamlit app streamlit run app/main.py

🚀 Features
✅ Converts SAS code to Python (pandas-based)
✅ Upload one or multiple files at once
✅ Clean, readable, executable output
✅ Timestamped folders for every conversion
✅ Supports both CLI and UI
✅ Optional REST API support
🛠 Tech Stack
🔁 Ollama – Local LLM backend (default: llama3)
🖥 Streamlit – Interactive UI
🧩 FastAPI – Optional API interface
🧾 Pydantic – Data validation
🔧 Python Subprocess – LLM invocation
🗂 dotenv + os – Environment and path management
