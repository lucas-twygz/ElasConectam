from django.db import models
from ckeditor.fields import RichTextField
from usuarios.models import Usuarios


class Postagens(models.Model):
    mensagem = RichTextField()
    autor = models.ForeignKey(Usuarios, on_delete=models.CASCADE, related_name='postagens')
    dataCriacao = models.DateTimeField(auto_now_add=True)

