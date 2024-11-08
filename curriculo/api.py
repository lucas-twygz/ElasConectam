from ninja import Router
from typing import List
from .models import Curriculo
from .schemas import CurriculoSchemaReq, CurriculoSchemaRes
from django.core.exceptions import ValidationError
from usuarios.models import Usuarios

curriculo_router = Router()

@curriculo_router.post("/curriculo/", response=CurriculoSchemaRes)
def create_curriculo(request, data: CurriculoSchemaReq):
    autor = Usuarios.objects.filter(id=data.autor_id).first()
    if not autor:
        raise ValidationError("Autor não encontrado")

    # Criar o currículo com o arquivo
    Curriculo.objects.create(
        titulo=data.titulo,
        arquivo=data.arquivo.file, 
        autor=autor
    )

    return {'msg': 'Currículo enviado com sucesso!'}

@curriculo_router.get("/curriculos/", response=List[CurriculoSchemaRes])
def get_all_curriculos(request):
    curriculos = Curriculo.objects.all()
    return curriculos
