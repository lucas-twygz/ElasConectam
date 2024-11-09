from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

class Vagas(models.Model):
    empresa = models.CharField(max_length=50, null=True)
    numeroDeCandidatos = models.IntegerField(default=0, null=False)
    titulo = models.CharField(max_length=50, null=False)
    descricao = RichTextField()
    dataDeCriacao = models.DateField(null=False)
    faixaSalarial = models.IntegerField(null=False)
    requisitos = models.CharField(max_length=255, null=False)
    candidatos = models.ManyToManyField(get_user_model(), related_name="vagas_inscritas", blank=True)
    
    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Vaga"
        verbose_name_plural = "Vagas"