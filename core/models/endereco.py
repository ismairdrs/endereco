import uuid

from django.db import models


class Endereco(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.UUIDField(default=uuid.uuid4, editable=True)
    rua = models.CharField(max_length=255)
    complemento1 = models.CharField(max_length=255)
    complemento2 = models.CharField(max_length=255, blank=True, null=True)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=8)
    ponto_referencia = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    modificado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Rua: {self.rua} complemento: {self.complemento1}'
