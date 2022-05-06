from django.contrib import admin
from .models import UserModel


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ('id', 'usuario', 'email', 'token', 'telefone', 'date')
    list_display_links = ('id', 'usuario', 'email')
=======
    list_display = ('id', 'usuario', 'email', 'token', 'telefone')
    list_display_links = ('id', 'usuario', 'email')
    
>>>>>>> 92e95a22d24feb637e573bff7181e3cb8572e420
