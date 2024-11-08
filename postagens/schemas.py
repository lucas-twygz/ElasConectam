from pydantic import BaseModel
from ninja import ModelSchema
from .models import Postagens

class PostagensSchemaReq(BaseModel):
    mensagem: str
    autor_id: int

class PostagensSchemaRes(ModelSchema):
    class Config():
        model = Postagens
        model_fields = "__all__"


