from src.components.llm_handler import LLMHandler
from src.components.file_utils import read_file, write_file, create_dated_folder
from prompts.template import prompt_template
import os

class SASConverter:
    def __init__(self):
        self.llm = LLMHandler()

    def convert_file(self, input_path: str, output_path: str):
        sas_code = read_file(input_path)
        python_code = self.llm.convert(sas_code, prompt_template)
        write_file(output_path, python_code)

    def convert_multiple_files(self, input_files: list[str], output_base_dir: str):
        output_dir = create_dated_folder(output_base_dir)
        for file_path in input_files:
            filename = os.path.basename(file_path).replace(".sas", ".py")
            output_path = os.path.join(output_dir, filename)
            self.convert_file(file_path, output_path)
        return output_dir