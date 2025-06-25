import os
import datetime

def read_file(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(file_path: str, content: str):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def create_dated_folder(base_dir: str) -> str:
    date_str = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    path = os.path.join(base_dir, date_str)
    os.makedirs(path, exist_ok=True)
    return path