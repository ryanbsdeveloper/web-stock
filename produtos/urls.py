from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('user/sing-up/', views.SingUpView.as_view(), name='cadastrar'),
    path('user/sing-in/', views.SingInView.as_view(), name='entrar')
]
