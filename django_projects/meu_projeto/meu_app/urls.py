from django.urls import path
from . import views


urlpatterns = [
    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('clientes/<int:cliente_id>/', views.detalhe_cliente, name='detalhe_cliente'),
    path('produtos/', views.ListarProdutosView.as_view(), name='listar_produtos'),
]
