from src.components.llm_handler import LLMHandler
from src.components.file_utils import read_file, write_file, create_dated_folder
from prompts.template import prompt_template, chunked_prompt_template, emotive_prompt_template, chunked_emotive_prompt_template
from src.components.chunking import semantic_chunking
import os
from config.settings import settings
import re
import ast

class SASConverter:
    def __init__(self):
        self.llm = LLMHandler()
        self.retry_count = 0

    def convert_file(self, input_path: str, output_path: str):
        sas_code = read_file(input_path)
        chunks = semantic_chunking(sas_code, similarity_threshold=0.5)
        print(len(chunks))
        if len(chunks) > 1:
            self.convert_chunks(chunks, output_path)
        else:
            python_code = self.llm.convert(sas_code, emotive_prompt_template if settings.emotive_prompting else prompt_template)
            write_file(output_path, python_code)
            syntax = self.check_syntax(output_path)
            if syntax:
                return
            else:
                self.convert_file(input_path, output_path)

    def check_syntax(self, output_path: str):
        if self.retry_count < 5:
            with open(output_path, "r", encoding="utf-8") as f:
                try:
                    parser = ast.parse(f.read(), output_path)
                except:
                    print("Error when parsing compiled code trying again.")
                    self.retry_count += 1
                    return False
            return True
        else:
            raise Exception("Attempted to convert code 5 times but failed. Syntax errors keep occuring")

    def convert_multiple_files(self, input_files: list[str], output_base_dir: str):
        output_dir = create_dated_folder(output_base_dir)
        self.retry_count = 0
        for file_path in input_files:
            filename = os.path.basename(file_path).replace(".sas", ".py")
            output_path = os.path.join(output_dir, filename)
            self.convert_file(file_path, output_path)
        return output_dir
    
    def remove_import_statements(self, code: str) -> str:
        cleaned = re.sub(r'^\s*(import|from\s+\S+\s+import)\s+.*$', '', code, flags=re.MULTILINE)
        return cleaned
    
    def convert_chunks(self, chunks: list[str], output_path: str):
        combined_code = ""
        for i, chunk in enumerate(chunks):
            if i == 0:
                combined_code += self.llm.convert(chunk, emotive_prompt_template if settings.emotive_prompting else prompt_template) + "\n"
            else:
                converted_code = self.llm.convert(chunk, chunked_emotive_prompt_template if settings.emotive_prompting else chunked_prompt_template) + "\n"
                converted_code = self.remove_import_statements(converted_code)
                combined_code += converted_code
        
        write_file(output_path, combined_code)
        syntax = self.check_syntax(output_path)
        if syntax:
            return
        else:
            self.convert_chunks(chunks, output_path)
