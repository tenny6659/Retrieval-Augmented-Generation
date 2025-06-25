import subprocess
import re
from config.settings import settings

class LLMHandler:
    def __init__(self):
        self.model = settings.model_name

    def convert(self, sas_code: str, prompt_template: str) -> str:
        prompt = prompt_template.format(sas_code=sas_code)
        process = subprocess.Popen(
            ["ollama", "run", self.model],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8'
        )

        stdout, stderr = process.communicate(prompt)
        if process.returncode != 0:
            raise RuntimeError(f"Ollama Error: {stderr}")

        # STEP 1: Try to extract the last triple-backtick code block
        matches = re.findall(r"```(?:python)?\s*([\s\S]*?)```", stdout, re.IGNORECASE)
        if matches:
            return matches[-1].strip()

        # STEP 2: Fallback – strip out explanation lines before they begin
        lines = stdout.splitlines()
        code_lines = []
        explanation_keywords = ("step", "explanation", "here's", "run this", "note:", "description")
        for line in lines:
            lstrip = line.strip().lower()
            if any(kw in lstrip for kw in explanation_keywords):
                break
            code_lines.append(line)

        return "\n".join(code_lines).strip()


