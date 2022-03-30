from django.forms import EmailInput
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .models import UserModel 
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from .forms import UserModel

class HomeView(TemplateView):
    template_name = 'index.html'


class SingUpView(CreateView):
    model = UserModel
    fields = '__all__'
    template_name = 'cadastrar.html'

    def post(self, request, *args, **kwargs):
        empresa = request.POST.get('empresa')
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        def form_valid(self, form):
            pass
        user = User.objects.create(username=usuario, email=email, password=senha)


        return HttpResponse(f'{user}')


class SingInView(CreateView):
    model = UserModel
    fields = '__all__'
    template_name = 'entrar.html'





    