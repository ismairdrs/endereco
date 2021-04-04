from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers

from core.api.v1.views import EnderecViewSet


router = routers.DefaultRouter()
router.register('', EnderecViewSet, basename='endereco')

urlpatterns = [
    url('', include(router.urls)),
]
