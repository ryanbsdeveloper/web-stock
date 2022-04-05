from django.shortcuts import render, redirect
from django.views.generic.base import View
from .forms import EstoqueForm
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin


class DashBoardView(View ,LoginRequiredMixin, AccessMixin):
    template_name = 'dashboard.html'
    login_url = 'home'
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
