from rest_framework import serializers

from core.api.v1.serializer import EnderecoSerializer
from core.models import Endereco


class EnderecViewSet(serializers.ModelSerializer):
    serializer_class = EnderecoSerializer

    def get_queryset(self, id):
        return Endereco.objects.filter(id=id)
