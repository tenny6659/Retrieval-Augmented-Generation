import streamlit as st
import os
import tempfile
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.components.convert import SASConverter


st.title(" CODEMORPH---SAS to Python Converter")

uploaded_files = st.file_uploader("Upload one or more .sas files", accept_multiple_files=True)

if uploaded_files:
    converter = SASConverter()
    input_paths = []
    for uploaded_file in uploaded_files:
        temp_path = os.path.join("data/input", uploaded_file.name)
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.read())
        input_paths.append(temp_path)

    output_dir = converter.convert_multiple_files(input_paths, "data/output")
    st.success(f"Converted {len(input_paths)} files. Output folder: {output_dir}")