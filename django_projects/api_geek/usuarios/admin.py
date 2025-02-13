from django.contrib import admin
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'date_joined', 'is_active')
    search_fields = ('username', 'email')
    list_filter = ('is_active', 'date_joined')
    ordering = ('date_joined',)

admin.site.register(Usuario, UsuarioAdmin)