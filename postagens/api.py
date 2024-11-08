from ninja import Router
from typing import List
from .models import Postagens
from .schemas import PostagensSchema
from django.http import Http404
from django.contrib.auth.models import User

postagem_router = Router()

@postagem_router.get('getTodasPostagens/', response=List[PostagensSchema])
def todasPostagens(request):
    postagensEncontradas = Postagens.objects.all()

    if postagensEncontradas.exists():
        return postagensEncontradas 
    else:
        raise Http404('Não foi encontrada nenhuma postagem')

@postagem_router.post('criarPostagem/')
def criarPostagem(request, novaPostagem: PostagensSchema):
    autor = request.user

    if not autor.is_authenticated:
        raise Http404('Usuário não autenticado.')

    Postagens.objects.create(
        mensagem=novaPostagem.mensagem,
        autor=autor,
        dataCriacao=novaPostagem.dataCriacao
    )

    return {'msg': 'Mensagem enviada com sucesso!'}
