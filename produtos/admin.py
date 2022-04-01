from django.contrib import admin
from .models import UserModel, EstoqueModel


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','empresa', 'usuario', 'email')
    list_display_links = ('id', 'empresa', 'usuario')


@admin.register(EstoqueModel)
class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('id','nome_produto', 'quantidade', 'preco',  'validade', 'usuario')
    list_display_links = ('id', 'nome_produto')

