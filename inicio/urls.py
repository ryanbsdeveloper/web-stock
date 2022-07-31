from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('doação/', views.DoaçãoView.as_view(), name='doação'),
    path('termos-de-uso/', views.TermosDeUso.as_view(), name='termos'),
    path('política-de-privacidade/', views.PoliticaDePrivacidade.as_view(), name='privacidade'),
    path('doc-api/', views.SobreView.as_view(), name='doc'),
    path('user/logout/', views.logout_view, name='sair'),
    path('user/sing-up/', views.SingUpView.as_view(), name='cadastrar'),
    path('user/auth/', views.AuthView.as_view(), name='auth'),
    path('user/sing-in/', views.SingInView.as_view(), name='entrar'),
]

