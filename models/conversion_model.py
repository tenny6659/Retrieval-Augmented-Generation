from pydantic import BaseModel

class ConversionRequest(BaseModel):
    sas_code: str

class ConversionResponse(BaseModel):
    python_code: str