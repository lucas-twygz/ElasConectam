from ninja import NinjaAPI
from usuarios.api import usuarios_router
from vagas.api import vagas_router
from postagens.api import postagens_router

api = NinjaAPI()

api.add_router('usuarios/', usuarios_router)
api.add_router('vagas/', vagas_router)
api.add_router('postagens/', postagens_router)