from trace import Trace
from django.db import models
from django.contrib.auth.models import User

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


class EstoqueModel(models.Model):
    usuario = models.ForeignKey(UserModel, related_name='estoque', on_delete=models.CASCADE, verbose_name='Usuário')
    nome_produto = models.CharField(max_length=50, verbose_name='Nome do produto')
    quantidade = models.IntegerField(verbose_name='Quantidade')
    validade = models.DateField(verbose_name='Validade do produto')
    marca = models.CharField(max_length=50, verbose_name='Marca do produto')
    preco = models.FloatField(verbose_name='Preço unitário ')


    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Estoque do usuário'