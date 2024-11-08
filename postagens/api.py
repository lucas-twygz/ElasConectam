from ninja import Router
from typing import List
from .models import Postagens
from .schemas import PostagensSchemaReq, PostagensSchemaRes
from django.http import Http404
from usuarios.models import Usuarios

postagens_router = Router()

@postagens_router.get('getTodasPostagens/', response=List[PostagensSchemaRes])
def todasPostagens(request):
    postagensEncontradas = Postagens.objects.all()

    if postagensEncontradas.exists():
        return postagensEncontradas 
    else:
        raise Http404('Não foi encontrada nenhuma postagem')

@postagens_router.post('criarPostagem/')
def criarPostagem(request, novaPostagem: PostagensSchemaReq):
    autor = Usuarios.objects.filter(id = novaPostagem.autor_id).first()

    Postagens.objects.create(
        mensagem = novaPostagem.mensagem,
        autor = autor
    )

    return {'msg': 'Mensagem enviada com sucesso!'}

@postagens_router.get('getPostagensDoUsuario/{usuario_id}/', response=List[PostagensSchemaRes])
def postagensDoUsuario(request, usuario_id: int):
    usuario = Usuarios.objects.get(id=usuario_id)

    postagensUsuario = usuario.postagens.all()

    return postagensUsuario
