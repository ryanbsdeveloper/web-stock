from django.forms import ModelForm
from .models import UserModel


class UserForm(ModelForm):
    def clean(self):
        data = self.cleaned_data
        senha =  data.get('senha')
        
        if len(senha) < 5:
            self.add_error('senha', 'Senha deve ter 5 caracteres ou mais.')
        

    class Meta:
        model = UserModel
        fields = '__all__'