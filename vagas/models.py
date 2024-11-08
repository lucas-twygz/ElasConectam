from django.db import models
from ckeditor.fields import RichTextField

class Vagas(models.Model):
    empresa = models.CharField(max_length=50, null=True)
    titulo = models.CharField(max_length=50, null=False)
    descricao = RichTextField()
    dataDeCriacao = models.DateField(null=False)
    faixaSalarial = models.IntegerField(null=False)
    requisitos = models.CharField(max_length=255, null=False)
    
    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Vaga"
        verbose_name_plural = "Vagas"