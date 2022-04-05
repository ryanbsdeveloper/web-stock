from django.contrib import admin
from .models import EstoqueModel
from django.contrib.auth.models import User


@admin.register(EstoqueModel)
class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('id','nome_produto', 'quantidade', 'preco',  'validade', 'usuario')
    list_display_links = ('id', 'nome_produto')
    def formfield_for_foreignkey(self, db_field, request, **kwargs):                
        if db_field.name == 'user': kwargs['queryset'] = User.objects.filter(user=request.user)  

