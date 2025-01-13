from django.contrib import admin
from core.models import Montadora, ModeloVeiculo


@admin.register(Montadora)
class MontadoraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'pais', 'ano_fundacao')
    search_fields = ('nome', 'pais')
    list_filter = ('pais',)


@admin.register(ModeloVeiculo)
class ModeloVeiculoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'motorizacao',)
    search_fields = ('nome', 'motorizacao')
    list_filter = ('motorizacao',)


# admin.site.register(Montadora, MontadoraAdmin)
