from ninja import ModelSchema
from .models import Vagas

class VagasSchema(ModelSchema):
    class Config:
        model = Vagas
        model_fields = "__all__"

class RegistroVagas(ModelSchema):
    class Config:
        model = Vagas
        model_fields = "__all__"