from django.contrib import admin
from .models import UserModel


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'usuario', 'email')
    list_display_links = ('empresa', 'usuario')

