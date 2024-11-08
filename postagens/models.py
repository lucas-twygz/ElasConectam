from django.db import models
from ckeditor.fields import RichTextField
from usuarios.models import Usuarios


class Postagens(models.Model):
    mensagem = RichTextField()
    autor = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    dataCriacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo