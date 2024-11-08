from django.db import models
from django.core.validators import FileExtensionValidator
from usuarios.models import Usuarios

class Curriculo(models.Model):
    titulo = models.CharField(max_length=100, null=True)
    autor = models.ForeignKey(Usuarios, on_delete=models.CASCADE, related_name='curriculos')
    arquivo = models.FileField(upload_to='curriculos/', validators=[FileExtensionValidator(allowed_extensions=['pdf'])], null=True
    )

    def __str__(self):
        return self.titulo
