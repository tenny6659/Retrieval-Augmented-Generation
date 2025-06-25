import time, os
from src.components.convert import SASConverter

WATCH_DIR = "data/input"
OUTPUT_BASE_DIR = "data/output"
converter = SASConverter()

def watch():
    seen_files = set()
    while True:
        files = [os.path.join(WATCH_DIR, f) for f in os.listdir(WATCH_DIR) if f.endswith(".sas")]
        new_files = [f for f in files if f not in seen_files]
        if new_files:
            converter.convert_multiple_files(new_files, OUTPUT_BASE_DIR)
            seen_files.update(new_files)
        time.sleep(10)