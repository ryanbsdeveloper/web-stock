from django.urls import path
from . import views

urlpatterns = [
    path('user/dashboard', views.DashBoardView.as_view(), name='dashboard'),
]
