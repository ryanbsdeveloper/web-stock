from django.contrib import admin
from .models import UserModel, EstoqueModel
from django.contrib.auth.models import User


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'email')
    list_display_links = ('id', 'usuario')


@admin.register(EstoqueModel)
class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('id','nome_produto', 'quantidade', 'preco',  'validade', 'usuario')
    list_display_links = ('id', 'nome_produto')
    def formfield_for_foreignkey(self, db_field, request, **kwargs):                
        if db_field.name == 'user': kwargs['queryset'] = User.objects.filter(user=request.user)  

