from rest_framework import viewsets, mixins

from core.api.v1.serializer import EnderecoSerializer
from core.models import Endereco


class EnderecViewSet(viewsets.GenericViewSet,
                    mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
