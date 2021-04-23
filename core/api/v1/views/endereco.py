from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError
import django_filters.rest_framework
from core.api.v1.serializer import EnderecoSerializer
from core.models import Endereco
from django.shortcuts import get_object_or_404

class EnderecViewSet(viewsets.ModelViewSet):
    serializer_class = EnderecoSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

    def get_queryset(self):
        usuario = self.request.query_params.get('usuario')
        if usuario:
            queryset = self.buscar_endereco_usuario(usuario)
        else:
            content = {'Requisição inválida': 'ID do usuário é obrigatório no query params /?usuario=id'}
            raise ValidationError(content)
        return queryset

    def buscar_endereco_usuario(self, usuario):
        try:
            queryset = Endereco.objects.filter(usuario=usuario)
        except:
            content = {'error': 'ID inválido'}
            raise ValidationError(content)
        return queryset