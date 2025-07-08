import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    def __init__(self):
        self.model_name = os.getenv("MODEL_NAME", "llama3")
        self.emotive_prompting = False

settings = Settings()