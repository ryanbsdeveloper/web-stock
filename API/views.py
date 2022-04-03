from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from produtos.models import EstoqueModel
from .serializers import EstoqueSerializer

class EstoqueViewSet(ModelViewSet):
    queryset = EstoqueModel.objects.all()
    serializer_class = EstoqueSerializer

    def get_queryset(self):
        print(':)')