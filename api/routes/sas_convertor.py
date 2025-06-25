from fastapi import APIRouter, UploadFile, File
from models.conversion_model import ConversionRequest, ConversionResponse
from src.components.llm_handler import LLMHandler
from prompts.template import prompt_template

router = APIRouter()
llm = LLMHandler()

@router.post("/convert", response_model=ConversionResponse)
def convert_code(req: ConversionRequest):
    result = llm.convert(req.sas_code, prompt_template)
    return ConversionResponse(python_code=result)