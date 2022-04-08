from django import forms
from .models import EstoqueModel


class EstoqueForm(forms.ModelForm):
    class Meta:
        model = EstoqueModel
        fields = ('nome_produto', 'imagem_produto',
                  'quantidade', 'validade', 'marca', 'preco')

