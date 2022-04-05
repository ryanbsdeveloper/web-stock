from django.shortcuts import render, redirect
from django.views.generic.base import View
from .forms import EstoqueForm
from inicio.models import UserModel
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib import auth
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin


class DashBoardView(LoginRequiredMixin ,View):
    template_name = 'dash.html'

    def setup(self, request, *args, **kwargs):
        self.token_valido_ou_n = UserModel.objects.get(usuario=request.user).token
        super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if not self.token_valido_ou_n:
                t = Token.objects.get_or_create(user=request.user)[0]
                # enviando email
                send_mail(
                    'Verificação rbs',
                    f'''
                    A equipe RBS agradece sua inscrição :) 
                    Token de verificação: {t}
                    *obs:Esse Token é para acesso externo do servidor.''', 
                    f'{settings.EMAIL_HOST_USER}',
                    [f'{request.user.email}'], fail_silently=False)
                
                return redirect('auth')
        
        return render(request, self.template_name)
    

    def post(self, request, *args, **kwargs):
        pass
