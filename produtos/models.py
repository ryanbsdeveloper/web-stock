from django.db import models
from django.forms import forms

class EstoqueModel(models.Model):
    foto_produto = models.ImageField()
    nome_produto = models.CharField()
    quantidade = models.DecimalField()
    validade = models.DateTimeField()
    marca = models.CharField()
    preco = models.Value()


class UserModel(models.Model):
    empresa = models.CharField(max_length=50, verbose_name='Empresa')
    usuario = models.CharField(max_length=50, verbose_name='Usuário')
    email = models.EmailField(unique=True, verbose_name='E-mail')
    senha = models.CharField(max_length=50, verbose_name='Senha')

    def __str__(self) -> str:
        return self.usuario

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
