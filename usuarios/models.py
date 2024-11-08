from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuarios(AbstractUser):
    email = models.EmailField(unique=True, null=False)
    dataNascimento = models.DateField(null=False)
    telefone = models.CharField(max_length=15, null=False)
    endereco = models.CharField(max_length=200, null=False)
    cpf = models.CharField(max_length=11, unique=True, null=False)
    cep = models.CharField(max_length=8, null=False)
    def __str__ (self):
        return self.first_name