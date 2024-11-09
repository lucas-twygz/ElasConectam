from ninja import Router
from .models import Vagas
from usuarios.models import Usuarios 
from .schemas import VagasSchema, RegistroVagas
from django.http import JsonResponse
from typing import List
import jwt
from django.conf import settings
from django.db import transaction

vagas_router = Router()

@vagas_router.get('getVagas/', response=List[VagasSchema])
def getTodasVagas(request):
    return Vagas.objects.all()

@vagas_router.post('registrarVagas/', response={200: str, 400: str})
def registrarVaga(request, novaVaga: RegistroVagas):
    vaga_encontrada = Vagas.objects.filter(titulo=novaVaga.titulo).first()

    if vaga_encontrada:
        return vagas_router.create_response(
            request, 'Essa vaga já está cadastrado.', status=400
        )

    Vagas.objects.create(
        empresa=novaVaga.empresa,
        titulo=novaVaga.titulo,
        numeroDeCandidatos=novaVaga.numeroDeCandidatos,
        descricao=novaVaga.descricao,
        dataDeCriacao=novaVaga.dataDeCriacao,
        faixaSalarial=novaVaga.faixaSalarial,
        requisitos=novaVaga.requisitos
    )

    return 'Vaga cadastrada com sucesso!'

@vagas_router.get('getVaga/{VagaId}/', response=VagasSchema)
def getVagaPorId(request, VagaId: int):
    try:
        vaga = Vagas.objects.get(id=VagaId)
        return vaga
    except:
        return JsonResponse({'detail': 'Vaga não encontrada!'}, status=404)
    
@vagas_router.post('candidatar/{VagaId}/', response={200: VagasSchema, 400: str, 401: str, 404: str})
def candidatar_vaga(request, VagaId: int):
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return JsonResponse({'detail': 'Token de autenticação não fornecido.'}, status=401)

    try:
        token = auth_header.split(" ")[1]
        payload = jwt.decode(token, settings.SECRET_KEY_JWT, algorithms=["HS256"])
        username = payload.get("user")

        usuario = Usuarios.objects.filter(username=username).first()
        if not usuario:
            return JsonResponse({'detail': 'Usuário não encontrado.'}, status=404)

        vaga = Vagas.objects.filter(id=VagaId).first()
        if not vaga:
            return JsonResponse({'detail': 'Vaga não encontrada.'}, status=404)

        if usuario in vaga.candidatos.all():
            return JsonResponse({'detail': 'Você já está inscrito nesta vaga.'}, status=400)

        with transaction.atomic():
            vaga.candidatos.add(usuario)
            vaga.numeroDeCandidatos += 1
            vaga.save()

        return vaga

    except jwt.ExpiredSignatureError:
        return JsonResponse({'detail': 'Token expirado.'}, status=401)
    except jwt.InvalidTokenError:
        return JsonResponse({'detail': 'Token inválido.'}, status=401)
