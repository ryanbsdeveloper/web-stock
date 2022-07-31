from django.contrib import admin
from .models import UserModel


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'email', 'token', 'telefone', 'date')
    list_display_links = ('id', 'usuario', 'email')
