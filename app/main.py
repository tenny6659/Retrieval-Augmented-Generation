import streamlit as st
import os
import tempfile
import sys
import os
from concurrent.futures import ThreadPoolExecutor
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.components.convert import SASConverter

st.title("CODEMORPH — SAS to Python Converter")

uploaded_files = st.file_uploader("Upload one or more .sas files", accept_multiple_files=True)

def convert_file_threadsafe(converter, input_path, output_dir):
    try:
        converter.convert_multiple_files([input_path], output_dir)
        return True, input_path
    except Exception as e:
        return False, f"{input_path} failed: {e}"

if uploaded_files:
    converter = SASConverter()
    input_paths = []

    for uploaded_file in uploaded_files:
        temp_path = os.path.join("data/input", uploaded_file.name)
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.read())
        input_paths.append(temp_path)

    output_dir = "data/output"
    st.info("Starting parallel file conversions...")

    results = []
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(convert_file_threadsafe, converter, path, output_dir) for path in input_paths]
        for future in futures:
            result = future.result()
            results.append(result)

    # Report results
    success_count = sum(1 for r in results if r[0])
    failed_files = [r[1] for r in results if not r[0]]

    st.success(f"Converted {success_count} file(s). Output folder: {output_dir}")
    if failed_files:
        st.error("Failed to convert the following files:")
        for fail in failed_files:
            st.text(fail)
