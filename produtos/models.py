from django.db import models
from django.contrib.auth import get_user_model


class EstoqueModel(models.Model):
    usuario = models.ForeignKey(get_user_model(), related_name='estoque', on_delete=models.CASCADE, blank=True, null=True)
    nome_produto = models.CharField(max_length=50, verbose_name='Nome do produto')
    imagem_produto = models.ImageField(upload_to='produtos-img/%Y')
    quantidade = models.IntegerField(verbose_name='Quantidade', default=1, blank=False)
    validade = models.CharField(max_length=50, verbose_name='Validade do produto',null=True, blank=True)
    marca = models.CharField(max_length=50, verbose_name='Marca do produto')
    preco = models.FloatField(verbose_name='Preço unitário ')
    created_at = models.DateTimeField(auto_now_add=True,  null=True)


    def __str__(self) -> str:
        return self.nome_produto

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Estoque do usuário'

