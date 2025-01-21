from django.contrib import admin
from controller.models import Projeto, Equipe, Membro, Atividade


# Register your models here.
class AtividadeInline(admin.TabularInline):
    model = Atividade
    extra = 1
    fields = ('nome', 'descricao', 'data_limite', 'feito', 'membro')
    show_change_link = True


class MembroInline(admin.TabularInline):
    model = Membro
    extra = 1
    fields = ('nome', 'funcao')
    show_change_link = True


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'data_inicio', 'data_final', 'equipe', 'duracao', 'quantidade_atividades')
    search_fields = ('nome', 'descricao', 'equipe__nome')
    list_filter = ('data_inicio', 'data_final', 'equipe__nome')
    inlines = [AtividadeInline]


@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'quantidade_membros')
    search_fields = ('nome',)
    list_filter = ('nome',)
    inlines = [MembroInline]


@admin.register(Membro)
class MembroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'funcao', 'equipe', 'quantidade_atividades')
    search_fields = ('nome', 'funcao', 'equipe__nome')
    list_filter = ('funcao', 'equipe__nome')


@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'data_limite', 'feito', 'projeto', 'membro', 'atrasada')
    search_fields = ('nome', 'descricao', 'projeto__nome', 'membro__nome')
    list_filter = ('data_limite', 'feito', 'projeto__nome', 'membro__nome')
