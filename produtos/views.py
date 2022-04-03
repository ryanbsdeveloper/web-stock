from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.base import View
from .models import UserModel
from .forms import UserForm, EstoqueForm
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib import auth
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail

import requests


def logout_view(request):
    auth.logout(request)
    return redirect('home')

class HomeView(TemplateView):
    template_name = 'index.html'
    

class SingUpView(View):
    template_name = 'cadastrar.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        self.usuario = request.POST.get('usuario')
        self.email = request.POST.get('email')
        self.senha = request.POST.get('senha')

        self.contexto = {
            'form': UserForm(request.POST or None),
            'recaptcha_site_key':settings.GOOGLE_RECAPTCHA_SITE_KEY,
        }

    def get(self, request):

        return render(request, self.template_name, self.contexto)

    def post(self, request, *args, **kwargs):
        form = self.contexto['form']

        if form.is_valid():
            '''reCAPTCHA'''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
            }
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()            
            '''fim do reCAPTCHA'''

            if result['success']:
                form.save()
                user = User.objects.create_user(username=self.usuario, email=self.email, password=self.senha)
                user.save()
                user_valida = auth.authenticate(username=self.usuario, password=self.senha)
                auth.login(request, user_valida )

                # token
                t = Token.objects.get_or_create(user=request.user)

                # enviando email
                send_mail(
                    'Verificação rbs',
                    f'''
                    A equipe RBS agradece sua inscrição :) 
                    Token de verificação: {t[0]}
                    *obs:Esse Token é para acesso externo do servidor.''', 
                    f'{settings.EMAIL_HOST_USER}',
                    [f'{self.email}'], fail_silently=False)
                

                return redirect('dashboard')
            else:
                messages.error(request, 'reCAPTCHA inválido')
                return render(request, self.template_name, self.contexto)

        return render(request, self.template_name, self.contexto)


class SingInView(View):
    template_name = 'entrar.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        self.contexto = {
            'form': UserForm(request.POST or None)
        }

    def get(self, request):
        return render(request, self.template_name, self.contexto)

    def post(self, request):
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        try:
            user = User.objects.get(email=email).username
        except:
            messages.error(request, 'O usuário que você inseriu não está conectado a uma conta.')
            return render(request, self.template_name, self.contexto )
        else:
            user_valida = auth.authenticate(username=user, password=senha)
            
            if user_valida:
                auth.login(request, user_valida )
                return redirect('dashboard')
            else:
                messages.error(request, 'A senha digitada não é válida.')
                return render(request, self.template_name, self.contexto)



class DashBoardView(LoginRequiredMixin, View):
    template_name = 'dashboard.html'
    login_url = 'entrar'
    redirect_field_name = 'dashboard'

    def setup(self, request, *args, **kwargs):

        self.contexto = {
            'form': EstoqueForm(request.POST or None, initial={'nome_produto': f'{request.user}'})
        }

        super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        t = Token.objects.get_or_create(user=request.user)
        print(':)') 
        return render(request, self.template_name, self.contexto)
    


    def post(self, request, *args, **kwargs):
        pass


    