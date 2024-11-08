from pydantic import BaseModel
from ninja import ModelSchema
from ninja.files import UploadedFile
from typing import ClassVar 
from .models import Curriculo

class CurriculoSchemaReq(BaseModel):
    titulo: str
    arquivo: UploadedFile
    autor_id: int

class CurriculoSchemaRes(ModelSchema):
    class Config:
        model = Curriculo
        model_fields = "__all__"
        orm_mode: ClassVar[bool] = True 

