from ninja import Router
from .schemas import UsuariosSchemaReq, UsuariosSchemaRes, usuarioLoginSchema
from .models import Usuarios
from typing import List
from django.http import Http404, JsonResponse
from django.conf import settings
from django.db.models import Q
from datetime import datetime, timedelta
#from djangoAPI.auth import JWTAuth
import jwt

usuarios_router = Router()

@usuarios_router.get("getTodos/", response=List[UsuariosSchemaRes])
def listar_usuarios(request):
    usuarios = Usuarios.objects.all()

    if usuarios.exists():
        return usuarios
    else:
        raise Http404("Não foram encontrados usuários.")

    
@usuarios_router.post("register/")
def registrarUsuario(request, novoUsuario: UsuariosSchemaReq):
    if Usuarios.objects.filter(email = novoUsuario.email).exists():
        raise Http404("Email já cadastrado")
    else:
        Usuarios.objects.create_user(**novoUsuario.dict())
        return JsonResponse({'msg': 'Usuário registrado com sucesso!'})
    
@usuarios_router.post("login/")
def logarUsuario(request, usuarioLogando: usuarioLoginSchema):
    usuarioEncontrado = Usuarios.objects.filter(
    Q(email=usuarioLogando.entrada) | 
    Q(username=usuarioLogando.entrada) | 
    Q(cpf=usuarioLogando.entrada)).first()

    if usuarioEncontrado and usuarioEncontrado.check_password(usuarioLogando.password):
        expiration_time = datetime.now() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE)
        print(f"Token expirando em: {expiration_time}")

        payload = {
            "user": usuarioEncontrado.username,
            "exp": int(expiration_time.timestamp())
        }

        token = jwt.encode(payload, settings.SECRET_KEY_JWT, algorithm="HS256")

        return {"token": token}
    else:
        raise Http404("Usuário não encontrado.")


    
