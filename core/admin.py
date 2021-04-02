from django.contrib import admin

from core.models import Endereco


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('rua', 'complemento1', 'complemento2', 'cidade', 'estado', 'cep')
