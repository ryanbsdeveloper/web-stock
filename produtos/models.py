from django.db import models
from django.contrib.auth import get_user_model


class EstoqueModel(models.Model):
    usuario = models.ForeignKey(get_user_model(), related_name='estoque', on_delete=models.CASCADE, blank=True, null=True)
    nome_produto = models.CharField(max_length=50, verbose_name='Nome do produto')
    quantidade = models.IntegerField(verbose_name='Quantidade')
    validade = models.DateField(verbose_name='Validade do produto')
    marca = models.CharField(max_length=50, verbose_name='Marca do produto')
    preco = models.FloatField(verbose_name='Preço unitário ')


    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Estoque do usuário'

    # def save(self, *args,**kwargs):
    #     self.nome_produto = 'a'

    #     super(EstoqueModel, self).save(*args,**kwargs)