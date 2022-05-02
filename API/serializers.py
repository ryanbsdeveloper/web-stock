from rest_framework.serializers import ModelSerializer, SerializerMethodField
from produtos.models import EstoqueModel
from django.contrib.auth import get_user_model

class EstoqueSerializer(ModelSerializer):

    class Meta:
        model = EstoqueModel
        fields = (
            'id',
            'nome_produto',
            'imagem_produto',
            'quantidade',
            'validade',
            'marca',
            'preco')
        read_only_fields = ['usuario']

    def validate(self, attrs):
        attrs['usuario'] = self.context['request'].user
        print(attrs)
        return attrs
