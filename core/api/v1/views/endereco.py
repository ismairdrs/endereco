from rest_framework import viewsets, mixins

from core.api.v1.serializer import EnderecoSerializer
from core.models import Endereco


class EnderecViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
