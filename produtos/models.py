from django.db import models
from django.forms import forms


class UserModel(models.Model):
    empresa = models.CharField(max_length=50, verbose_name='Empresa')
    usuario = models.CharField(max_length=50, verbose_name='Usuário')
    email = models.EmailField(unique=True, verbose_name='E-mail')
    senha = models.CharField(max_length=50, verbose_name='Senha')


    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
