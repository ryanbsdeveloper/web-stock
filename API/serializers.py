from rest_framework.serializers import ModelSerializer
from produtos.models import EstoqueModel

class EstoqueSerializer(ModelSerializer):
    class Meta:
        model = EstoqueModel
        fields = (
            'id',
            'usuario',
            'nome_produto',
            'quantidade',
            'validade',
            'marca',
            'preco')