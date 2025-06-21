# import chromadb
# #from dotenv import load_dotenv
# import requests  # Needed for Ollama API

# #python load_dotenv()

# # Paths
# DATA_PATH = r"data"
# CHROMA_PATH = r"chroma_db"

# # Set up ChromaDB
# chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
# collection = chroma_client.get_or_create_collection(
#     name="growing_vegetables"
# )

# # collection = chroma_client.get_or_create_collection(
# #     name="growing_vegetables",
# #     metadata={"hnsw:space": "cosine"},
# #     embedding_function=None,
# #     configuration={"hnsw:ef_construction": 200, "hnsw:M": 16, "num_threads": 2}
# # )

# # User input
# user_query = input("Ask Your Queries?\n\n")

# # # For Streamlit, read from file
# # try:
# #     with open("user_input.txt", "r", encoding="utf-8") as f:
# #         user_query = f.read().strip()
# # except FileNotFoundError:
# #     user_query = input("What do you want to know about growing vegetables?\n\n")


# # Retrieve relevant docs
# results = collection.query(
#     query_texts=[user_query],
#     n_results=4
# )
# print("\n[Top Chunks Retrieved from ChromaDB]\n")
# print(results['documents'])

# # Construct prompt for Ollama
# system_prompt = """
# You are a helpful assistant. You answer questions about growing vegetables in Florida. 
# But you only answer based on knowledge I'm providing you. You don't use your internal 
# knowledge and you don't make things up.
# If you don't know the answer, just say: I don't know
# --------------------
# The data:
# """ + str(results['documents']) + "\n\n"

# if "generate pyspark" in user_query.lower():
#     final_prompt = system_prompt + "Write PySpark code that:\n" + user_query
# else:
#     final_prompt = system_prompt + user_query

# # Use Ollama instead of OpenAI
# def query_ollama(prompt, model="mistral"):
#     response = requests.post(
#         "http://localhost:11434/api/generate",
#         json={"model": model, "prompt": prompt, "stream": False}
#     )
#     return response.json()["response"]

# # Generate response
# output = query_ollama(final_prompt)

# print("\n\n---------------------\n\n")
# print(output)

# # Save PySpark code if applicable
# if "generate pyspark" in user_query.lower():
#     with open("generated_spark.py", "w", encoding="utf-8") as f:
#         f.write(output)
#     print("[Saved] PySpark code in generated_spark.py")
# save = input("\n💾 Do you want to save the output to generate.py? (yes/no): ").strip().lower()
# if save == "yes":
#     with open("generate.py", "w", encoding="utf-8") as f:
#         f.write(output)
#     print("\n✅ Saved to generate.py")   




# import chromadb
# import requests
# import streamlit as st

# # Paths
# DATA_PATH = r"data"
# CHROMA_PATH = r"chroma_db"

# # Initialize ChromaDB
# chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
# collection = chroma_client.get_or_create_collection(name="growing_vegetables")

# # Streamlit UI
# st.title("🌿 Vegetable Growing Assistant")
# st.write("Ask a question related to growing vegetables in Florida.")

# user_query = st.text_input("❓ Your Question:")

# def query_ollama(prompt, model="mistral"):
#     response = requests.post(
#         "http://localhost:11434/api/generate",
#         json={"model": model, "prompt": prompt, "stream": False}
#     )
#     return response.json()["response"]

# if user_query:
#     # Retrieve documents from ChromaDB
#     results = collection.query(query_texts=[user_query], n_results=4)

#     st.subheader("🔍 Retrieved Chunks from ChromaDB")
#     for i, doc in enumerate(results['documents'][0]):
#         st.markdown(f"**Chunk {i+1}:** {doc}")

#     # Construct prompt for Ollama
#     system_prompt = """
#     You are a helpful assistant. You answer questions about growing vegetables in Florida. 
#     But you only answer based on knowledge I'm providing you. You don't use your internal 
#     knowledge and you don't make things up.
#     If you don't know the answer, just say: I don't know
#     --------------------
#     The data:
#     """ + str(results['documents']) + "\n\n"

#     if "generate pyspark" in user_query.lower():
#         final_prompt = system_prompt + "Write PySpark code that:\n" + user_query
#     else:
#         final_prompt = system_prompt + user_query

#     # Query Ollama
#     output = query_ollama(final_prompt)

#     st.subheader("💡 Assistant's Answer")
#     st.write(output)

#     # Option to save to PySpark file
#     if "generate pyspark" in user_query.lower():
#         with open("generated_spark.py", "w", encoding="utf-8") as f:
#             f.write(output)
#         st.success("✅ PySpark code saved to `generated_spark.py`")

#     # Option to save to generate.py
#     if st.checkbox("💾 Save response to generate.py"):
#         with open("generate.py", "w", encoding="utf-8") as f:
#             f.write(output)
#         st.success("✅ Output saved to `generate.py`")


#2nd streamlit
# import chromadb
# import requests
# import streamlit as st
# import os

# # --- Setup paths ---
# CHROMA_PATH = r"chroma_db"
# UPLOAD_DIR = "data"
# os.makedirs(UPLOAD_DIR, exist_ok=True)

# # --- Initialize ChromaDB ---
# chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
# collection = chroma_client.get_or_create_collection(name="growing_vegetables")

# # --- Streamlit UI ---
# st.title("🌿 AI Assistant")
# st.write("Upload your files and ask questions related to the content.")

# # --- File Upload ---
# uploaded_files = st.file_uploader("📂 Upload Files", accept_multiple_files=True, type=['txt','pdf','doc'], key="fileUploader")
# if uploaded_files:
#     st.success(f"✅ {len(uploaded_files)} file(s) uploaded")
#     for file in uploaded_files:
#         file_path = os.path.join(UPLOAD_DIR, file.name)
#         with open(file_path, "wb") as f:
#             f.write(file.read())

#         # For demo: Just add file content as separate documents to ChromaDB
#         with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
#             content = f.read()

#         collection.add(
#             documents=[content],
#             ids=[file.name]  # Ensure unique ID per document
#         )

# # --- User Input ---
# user_query = st.text_input("❓ Ask a Question:")

# def query_ollama(prompt, model="mistral"):
#     response = requests.post(
#         "http://localhost:11434/api/generate",
#         json={"model": model, "prompt": prompt, "stream": False}
#     )
#     return response.json()["response"]

# if user_query:
#     results = collection.query(query_texts=[user_query], n_results=4)

#     st.subheader("🔍 Top Chunks Retrieved")
#     for i, doc in enumerate(results['documents'][0]):
#         st.markdown(f"**Chunk {i+1}:** {doc}")

#     system_prompt = """
#     You are a helpful assistant. You answer questions only based on the provided content. 
#     Don't use internal knowledge. If unsure, say "I don't know".
#     --------------------
#     The data:
#     """ + str(results['documents']) + "\n\n"

#     final_prompt = system_prompt + ("Write PySpark code that:\n" if "generate pyspark" in user_query.lower() else "") + user_query
#     output = query_ollama(final_prompt)

#     st.subheader("💡 Answer")
#     st.write(output)

#     if st.checkbox("💾 Save answer to generate.py"):
#         with open("generate.py", "w", encoding="utf-8") as f:
#             f.write(output)
#         st.success("✅ Output saved to `generate.py`")

#     if "generate pyspark" in user_query.lower():
#         with open("generated_spark.py", "w", encoding="utf-8") as f:
#             f.write(output)
#         st.success("✅ PySpark code saved to `generated_spark.py`")

#3rd streamlit



import chromadb
import requests
import streamlit as st
import os
import pdfplumber  # <-- Make sure this is installed: pip install pdfplumber

# Setup
CHROMA_PATH = "chroma_db"
UPLOAD_DIR = "data"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Initialize ChromaDB
chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)

# ⚠️ Option 1: Automatically delete collection each run
try:
    chroma_client.delete_collection("growing_vegetables")
except:
    pass

collection = chroma_client.get_or_create_collection(name="growing_vegetables")

# Streamlit UI
st.title("🌿  AI PromptFlow")
st.markdown("Upload `.pdf` or `.txt` files. Ask questions based on them.")

# 🧹 Optional: Manual ChromaDB reset
if st.button("♻️ Reset ChromaDB"):
    chroma_client.delete_collection("growing_vegetables")
    collection = chroma_client.get_or_create_collection(name="growing_vegetables")
    st.success("✅ ChromaDB has been reset.")

# Upload files
uploaded_files = st.file_uploader("📂 Upload Files", type=["pdf", "txt"], accept_multiple_files=True)

def extract_text(file, extension):
    if extension == "txt":
        return file.read().decode("utf-8", errors="ignore")
    elif extension == "pdf":
        with pdfplumber.open(file) as pdf:
            return "\n".join([page.extract_text() or '' for page in pdf.pages])
    return ""

if uploaded_files:
    for file in uploaded_files:
        ext = file.name.split(".")[-1].lower()
        file_path = os.path.join(UPLOAD_DIR, file.name)

        with open(file_path, "wb") as f:
            f.write(file.read())

        with open(file_path, "rb") as f:
            content = extract_text(f, ext)

        if content.strip():
            collection.add(documents=[content], ids=[file.name])
        else:
            st.warning(f"⚠️ No text extracted from {file.name}. Skipped.")

    st.success(f"✅ Uploaded and processed {len(uploaded_files)} file(s).")

# Query Input
user_query = st.text_input("❓ Ask your question:")

def query_ollama(prompt, model="mistral"):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": model, "prompt": prompt, "stream": False}
        )
        return response.json()["response"]
    except Exception as e:
        return f"❌ Ollama error: {e}"

if user_query:
    results = collection.query(query_texts=[user_query], n_results=4)

    st.subheader("🔍 Top Chunks Retrieved")
    for i, doc in enumerate(results['documents'][0]):
        st.markdown(f"**Chunk {i+1}:** {doc.strip()[:500]}...")  # limit output

    system_prompt = """
    You are a helpful assistant. Only use the provided content to answer. 
    If you don’t know the answer, just say: "I don’t know".
    --------------------
    The data:
    """ + str(results['documents']) + "\n\n"

    final_prompt = system_prompt
    if "generate pyspark" in user_query.lower():
        final_prompt += "Write PySpark code that:\n" + user_query
    else:
        final_prompt += user_query

    output = query_ollama(final_prompt)

    st.subheader("💡 Answer")
    st.write(output)

    if st.checkbox("💾 Save response to `generate.py`"):
        with open("generate.py", "w", encoding="utf-8") as f:
            f.write(output)
        st.success("✅ Saved to `generate.py`")

    if "generate pyspark" in user_query.lower():
        with open("generated_spark.py", "w", encoding="utf-8") as f:
            f.write(output)
        st.success("✅ PySpark code saved to `generated_spark.py`")
