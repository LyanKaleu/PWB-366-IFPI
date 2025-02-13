from django.contrib import admin
from .models import Produto, Cliente, Pedido


admin.site.register(Produto)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'criado_em')
    search_fields = ('nome', 'email')
    list_filter = ('criado_em',)
