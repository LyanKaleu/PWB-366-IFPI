from django.contrib import admin
from .models import Venda, ItemVenda


class ItemVendaInline(admin.TabularInline):
    model = ItemVenda
    extra = 1


@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'valor_total', 'data_venda']
    list_filter = ['data_venda']
    search_fields = ['cliente']
    inlines = [ItemVendaInline]
    