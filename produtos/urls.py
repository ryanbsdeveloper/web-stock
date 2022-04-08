from django.urls import path

from . import views

urlpatterns = [
    path('user/dashboard', views.DashBoardView.as_view(), name='dashboard'),
    path('user/seu-estoque', views.ProdutosView.as_view(), name='produtos'),
    path('user/seu-estoque/del/<int:id>', views.DelProduto, name='produtos'),

]