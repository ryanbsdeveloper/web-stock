from django import forms
from .models import EstoqueModel


class EstoqueForm(forms.ModelForm):
    def clean(self):
        quantidade = self.cleaned_data['quantidade']
        telefone = self.cleaned_data['telefone']

        if telefone:
            if telefone < 11 or not telefone.isnumeric():
                self.add_error('telefone', 'Esse número de telefone não é válido.') 

        if quantidade < 0:
            self.add_error('quantidade', 'Quantidade de produtos não pode ser menor que 0.')
        
    class Meta:
        model = EstoqueModel
        fields = ('nome_produto', 'imagem_produto',
                  'quantidade', 'validade', 'marca', 'preco')

