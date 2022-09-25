from django.urls import path

from . import views
from Estoque.views import notfound404

handler404 = notfound404

urlpatterns = [
    path('user/dashboard', views.DashBoardView.as_view(), name='dashboard'),
    path('user/seu-estoque', views.ProdutosView.as_view(), name='produtos'),
    path('user/seu-estoque/del/<int:id>', views.DelProduto, name='deletar'),
    path('user/seu-estoque/edit/<int:id>', views.EditarView.as_view(), name='editar'),
]