from django.contrib import admin
from .models import Postagens

class PostagensAdmin(admin.ModelAdmin):
    list_display = ('mensagem', 'autor', 'dataCriacao')
    search_fields = ('mensagem', 'autor__username')
    list_filter = ('dataCriacao', 'autor')

admin.site.register(Postagens, PostagensAdmin)