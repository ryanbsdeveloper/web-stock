from django.shortcuts import render, redirect
from django.views import View
from inicio.models import UserModel
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin
from .utils import mês


class SenhaView(LoginRequiredMixin, View):
    template_name = 'senha.html'

    def setup(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().setup(request, *args, **kwargs)

        self.user_model = UserModel.objects.get(usuario=request.user)
        self.user_valida = auth.authenticate(username=self.user_model.usuario, password=self.user_model.senha)
        print(self.user_valida)

        super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        senha = request.POST.get('senha1')
        check_senha = request.POST.get('senha2')
        if senha != check_senha:
            messages.error(request, 'Senhas não conferem')
            return render(request, self.template_name)

        if len(senha) < 5:
            messages.error(request, 'Senha deve ter 5 caracteres ou mais.')
            return render(request, self.template_name)
        
        messages.success(request, 'Sua senha foi alterada com sucesso.')

        self.user_valida.set_password(senha)
        self.user_valida.save()
        self.user_model.senha = senha
        self.user_model.save()
        auth.login(request, self.user_valida)
        return redirect('dashboard')


class PerfilView(LoginRequiredMixin, View):
    template_name = 'perfil.html'

    def setup(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().setup(request, *args, **kwargs)

        user = UserModel.objects.all().filter(usuario=request.user).values()
        token = Token.objects.get_or_create(user=request.user)[0]
        senha = user[0]['senha']
        telefone = user[0]['telefone']
        data = user[0]['created_at']
        data = f'{mês(data.month)} de {data.year}'
        print(data)
        self.contexto = {
            'token': token,
            'senha': senha,
            'telefone': telefone,
            'data':data,
        }
        super().setup(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.contexto)

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(UserModel, pk=request.user.id)
        telefone = request.POST.get('telefone')
        if len(telefone) < 11 or not telefone.isnumeric():
            if len(telefone) == 0:
                messages.error(request, 'Sem número para verificar')
                return render(request, self.template_name, self.contexto)

            messages.error(request, 'Número de telefone não está válido.')
            return render(request, self.template_name, self.contexto)
        user.telefone = telefone
        user.save()
        return redirect('perfil')


class APIView(LoginRequiredMixin, View):
    template_name = 'api.html'

    def setup(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().setup(request, *args, **kwargs)
        
        super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        pass


class ExcluirContaView(LoginRequiredMixin, View):
    template_name = 'excluir.html'

    def setup(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().setup(request, *args, **kwargs)

        super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request,  self.template_name)

    def post(self, request, *args, **kwargs):
        pass