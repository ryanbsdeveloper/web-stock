from django import forms
from .models import UserModel


class UserForm(forms.ModelForm):
    def clean(self):
        data = self.cleaned_data
        senha =  data.get('senha')
        usuario = data.get('usuario')
        email = data.get('email')
        todos_os_emails = UserModel.objects.all().values_list('email', flat=True)
        todos_os_usuarios = UserModel.objects.all().values_list('usuario', flat=True)

        if usuario in todos_os_usuarios:
            self.add_error('usuario', 'Conta com esse nome de usuário já existe.')

        if email in todos_os_emails:
            self.add_error('email', 'Conta com este E-mail já existe.')
       
        if len(senha) < 5:
            self.add_error('senha', 'Senha deve ter 5 caracteres ou mais.')
        

    class Meta:
        model = UserModel
        fields = ('usuario', 'email', 'senha', 'telefone')
        widgets = {
                'senha': forms.PasswordInput(),
            }
  