from django.urls import path

from . import views

urlpatterns = [
    path('user/perfil/', views.PerfilView.as_view(), name='perfil'),
    path('user/perfil/excluir-conta/', views.ExcluirContaView.as_view(), name='excluir'),
    path('user/perfil/alterar-senha/', views.SenhaView.as_view(), name='senha'),
]