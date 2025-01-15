from django.contrib import admin
from django.urls import path


admin.site.site_header = 'Gestão de Veículos'
admin.site.index_title = 'Cadastros'

urlpatterns = [
    path('admin/', admin.site.urls),
]
