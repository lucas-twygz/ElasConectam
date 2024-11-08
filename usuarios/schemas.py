from ninja import ModelSchema, Schema
from .models import Usuarios

class UsuariosSchemaRes(ModelSchema):
    class Config():
        model = Usuarios
        model_fields = "__all__"

class UsuariosSchemaReq(ModelSchema):
    class Config():
        model = Usuarios
        model_fields = ['username', 'email', 'password', 'dataNascimento', 'telefone', 'endereco', 'cpf', 'cep', 'first_name', 'last_name']


class usuarioLoginSchema(Schema):
    entrada: str
    password: str