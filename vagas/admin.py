from django.contrib import admin
from .models import Vagas


class VagasAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'titulo', 'faixaSalarial', 'dataDeCriacao')
    search_fields = ('titulo', 'empresa')
    list_filter = ('dataDeCriacao', 'faixaSalarial')

admin.site.register(Vagas, VagasAdmin)