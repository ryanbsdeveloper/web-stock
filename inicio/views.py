import email
from re import template
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.base import View
from .models import UserModel
from .forms import UserForm
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import auth
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.template.loader import render_to_string
import requests


def logout_view(request):
    auth.logout(request)
    return redirect('home')


class HomeView(TemplateView):
    template_name = 'index.html'

    def setup(self, request, *args, **kwargs) -> None:
        auth.logout(request)

        return super().setup(request, *args, **kwargs)


class SingUpView(View):
    template_name = 'cadastrar.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        self.usuario = request.POST.get('usuario')
        self.email = request.POST.get('email')
        self.senha = request.POST.get('senha')

        self.contexto = {
            'form': UserForm(request.POST or None),
            'email': self.email,
            'recaptcha_site_key': settings.GOOGLE_RECAPTCHA_SITE_KEY,
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
            r = requests.post(
                'https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()
            '''fim do reCAPTCHA'''

            if result['success']:
                form.save()
                user = User.objects.create_user(
                    username=self.usuario, email=self.email, password=self.senha)
                user.save()
                user_valida = auth.authenticate(
                    username=self.usuario, password=self.senha)
                auth.login(request, user_valida)

                # token
                t = Token.objects.get_or_create(user=request.user)[0]

                # enviar email
                html = render_to_string(
                    'email.html', {'token': t, 'nome': request.user})
                msg = strip_tags(html)

                send_mail('Verificação WEB Stock', msg, 'ryanbsdeveloper@gmail.com', [f'{self.email}'], html_message=html)
                return redirect('auth')
            else:
                messages.error(request, 'reCAPTCHA inválido')
                return render(request, self.template_name, self.contexto)

        return render(request, self.template_name, self.contexto)


class SingInView(View):
    template_name = 'entrar.html'

    def setup(self, request, *args, **kwargs):
        self.contexto = {
            'form': UserForm(request.POST or None),
        }
        super().setup(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, self.contexto)

    def post(self, request):
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        try:
            user = User.objects.get(email=email).username
        except:
            messages.error(
                request, 'O e-mail que você inseriu não está conectado a uma conta.')
            return render(request, self.template_name, self.contexto)
        else:
            user_valida = auth.authenticate(username=user, password=senha)
            token_valida_do_usuario = UserModel.objects.get(usuario=user).token

            if user_valida:

                auth.login(request, user_valida)
                t = Token.objects.get_or_create(user=request.user)[0]
                if not token_valida_do_usuario:
                    # enviar email
                    html = render_to_string(
                        'email.html', {'token': t, 'nome': request.user})
                    msg = strip_tags(html)
                    email = EmailMultiAlternatives(
                        'Verificação WEB Stock', msg, settings.EMAIL_HOST_USER, [f'{email}'])
                    email.attach_alternative(html, 'text/html')
                    email.send()

                    auth.login(request, user_valida)
                    return redirect('auth')

                return redirect('dashboard')
            else:
                messages.error(request, 'A senha digitada não é válida.')
                return render(request, self.template_name, self.contexto)


class AuthView(LoginRequiredMixin, View):
    template_name = 'auth.html'
    user = None

    def setup(self, request, *args, **kwargs):
        self.user = request.user
        if not self.user.is_authenticated:
            return super().setup(request, *args, **kwargs)

        self.token_valido_ou_n = UserModel.objects.get(
            usuario=self.user.username).token
        self.contexto = {
            'email': self.user.email
        }
        super().setup(request, *args, **kwargs)

    def get(self, request):
        if self.token_valido_ou_n:
            return redirect('dashboard')
        return render(request, self.template_name, self.contexto)

    def post(self, request, *args, **kwargs):
        input_token = request.POST.get('token')
        print(self.user.username)
        token_do_usuario = Token.objects.get_or_create(user=self.user)[0]
        user = UserModel.objects.get(usuario=self.user)
        if str(input_token) == str(token_do_usuario):
            valida_token = UserModel(
                id=user.id, usuario=user.usuario, email=user.email, senha=user.senha, token=True)
            valida_token.save()
            return redirect('dashboard')

        messages.error(request, 'Token não confere!')

        return render(request, self.template_name, self.contexto)


class DoaçãoView(TemplateView):
    template_name = 'doacao.html'


class SobreView(TemplateView):
    template_name = 'doc.html'


class PoliticaDePrivacidade(TemplateView):
    template_name = 'privacidade.html'


class TermosDeUso(TemplateView):
    template_name = 'termos.html'
