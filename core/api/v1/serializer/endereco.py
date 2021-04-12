from rest_framework import serializers

from core.models import Endereco


class EnderecoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Endereco
        fields = ('id', 'usuario', 'rua', 'complemento1', 'complemento2', 'cidade', 'estado', 'cep', 'ponto_referencia')
