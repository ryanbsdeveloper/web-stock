from django import forms
from .models import EstoqueModel

class EstoqueForm(forms.ModelForm):
    class Meta:
        model = EstoqueModel
        fields = '__all__'

