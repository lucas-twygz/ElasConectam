from ninja import Router
from .models import Vagas
from .schemas import VagasSchema, RegistroVagas
from django.http import JsonResponse
from typing import List

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