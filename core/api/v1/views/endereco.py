from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError
import django_filters.rest_framework
from core.api.v1.serializer import EnderecoSerializer
from core.models import Endereco


class EnderecViewSet(viewsets.ModelViewSet):
   # queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['usuario',]

    def get_queryset(self):

        user = self.request.query_params.get('usuario')
        if user:
            queryset = Endereco.objects.filter(usuario=user)
        else:
            content = {'Requisição inválida': 'ID do usuário é obrigatório no query params /?usuario=id'}
            raise ValidationError(content)
        return queryset
