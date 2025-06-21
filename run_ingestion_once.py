import os
import time

# path to the data folder and chroma
DATA_PATH = "data"

# Check if any new PDFs exist
pdfs = [f for f in os.listdir(DATA_PATH) if f.endswith(".pdf")]

if pdfs:
    print(f"[INFO] Found {len(pdfs)} PDFs in '{DATA_PATH}/'. Running fill_db.py...")
    os.system("python fill_db.py")
    print("[INFO] fill_db.py completed.")
else:
    print("[INFO] No PDFs found in 'data/' folder. Nothing to ingest.")


import time

while True:
    # the same check block...
    # then sleep:
    time.sleep(300)  # every 5 minutes
