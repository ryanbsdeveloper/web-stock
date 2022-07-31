from django.contrib import admin
from .models import EstoqueModel


@admin.register(EstoqueModel)
class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('id','nome_produto', 'quantidade', 'preco',  'validade', 'usuario')
    list_display_links = ('id', 'nome_produto')
    list_filter = ('usuario',)
