from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import TemplateHTMLRenderer
from produtos.models import EstoqueModel
from .serializers import EstoqueSerializer
from django.contrib.auth import get_user_model


class EstoqueViewSet(ModelViewSet):
    serializer_class = EstoqueSerializer

    def get_queryset(self):
        user = self.request.user
        return EstoqueModel.objects.filter(usuario=user)

