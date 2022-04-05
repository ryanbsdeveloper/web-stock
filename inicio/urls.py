from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('user/logout', views.logout_view, name='sair'),
    path('user/sing-up/', views.SingUpView.as_view(), name='cadastrar'),
    path('user/auth/', views.AuthView.as_view(), name='auth'),
    path('user/sing-in/', views.SingInView.as_view(), name='entrar'),
]

