from ninja import ModelSchema
from .models import Postagens

class PostagensSchema(ModelSchema):
    class Config():
        model = Postagens
        model_fields = "__all__"