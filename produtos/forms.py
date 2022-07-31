from django import forms
from .models import EstoqueModel


class EstoqueForm(forms.ModelForm):
    def clean(self):
        quantidade = self.cleaned_data['quantidade']

        if quantidade < 0:
            self.add_error('quantidade', 'Quantidade de produtos não pode ser menor que 0.')
        
    class Meta:
        model = EstoqueModel
        fields = ('nome_produto', 'imagem_produto',
                  'quantidade', 'validade', 'marca', 'preco')

