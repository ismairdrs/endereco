from rest_framework import serializers

from core.models import Endereco

serializers.ListSerializer
class EnderecoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Endereco
        fields = ('id', 'rua', 'complemento1', 'complemento2', 'cidade', 'estado', 'cep', 'ponto_referencia')
