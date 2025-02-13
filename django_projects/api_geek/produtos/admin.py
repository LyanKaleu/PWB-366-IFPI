from django.contrib import admin
from .models import Produto, Categoria, Franquia


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    search_fields = ['nome']


@admin.register(Franquia)
class FranquiaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    search_fields = ['nome']


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'preco', 'quantidade_estoque', 'categoria', 'franquia']
    list_filter = ['categoria', 'franquia']
    search_fields = ['nome']