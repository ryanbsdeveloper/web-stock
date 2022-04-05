from django import forms
from .models import UserModel


class UserForm(forms.ModelForm):
    def clean(self):
        data = self.cleaned_data
        senha =  data.get('senha')
        email = data.get('email')
        todos_os_emails = UserModel.objects.all().values_list('email', flat=True)

        if email in todos_os_emails:
            self.add_error('email', 'Usuário com este E-mail já existe.')
       
        if len(senha) < 5:
            self.add_error('senha', 'Senha deve ter 5 caracteres ou mais.')
        

    class Meta:
        model = UserModel
        fields = ('usuario', 'email', 'senha')
        widgets = {
                'senha': forms.PasswordInput(),
            }
  