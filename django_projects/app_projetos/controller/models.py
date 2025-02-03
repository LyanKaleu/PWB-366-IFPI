from django.db import models
from django.contrib import admin
import datetime


# Create your models here.
class Projeto(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    descricao = models.CharField(max_length=200, blank=False, null=False)
    data_inicio = models.DateField()
    data_final = models.DateField()
    equipe = models.OneToOneField(
        'Equipe', 
        on_delete=models.CASCADE,
        related_name='projeto'
    )

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
        ordering = ['nome']

    def __str__(self):
        return self.nome
    
    @admin.display(description='Duração do Projeto (dias)')
    def duracao(self):
        return (self.data_final - self.data_inicio).days
    
    @admin.display(description='Qtd Atividades')
    def quantidade_atividades(self):
        return self.atividades.count()


class Equipe(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipes'
        ordering = ['nome']
    
    def __str__(self):
        return self.nome
    
    @admin.display(description='Qtd Membros')
    def quantidade_membros(self):
        return self.membros.count()
    

class Membro(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    funcao = models.CharField(max_length=100, blank=False, null=False)
    equipe = models.ForeignKey( 
        'Equipe', 
        on_delete=models.CASCADE,
        related_name='membros'
    )

    class Meta:
        verbose_name = 'Membro'
        verbose_name_plural = 'Membros'
        ordering = ['nome']

    def __str__(self):
        return self.nome
    
    @admin.display(description='Qtd Atividades')
    def quantidade_atividades(self):
        return self.atividades.count()


class Atividade(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    descricao = models.CharField(max_length=200, blank=False, null=False)
    data_limite = models.DateField()
    feito = models.BooleanField(default=False)
    projeto = models.ForeignKey(
        'Projeto', 
        on_delete=models.CASCADE,
        related_name='atividades'
    )
    membro = models.ForeignKey(
        'Membro', 
        on_delete=models.CASCADE,
        related_name='atividades'
    )

    class Meta:
        verbose_name = 'Atividade'
        verbose_name_plural = 'Atividades'
        ordering = ['data_limite', 'nome']

    def __str__(self):
        return self.nome
    
    @admin.display(description='Atrasada?')
    def atrasada(self):
        return not self.feito and self.data_limite < datetime.date.today()


class Comentario(models.Model):
    texto = models.TextField('Comentário', max_length=500, blank=False, null=False)
    criado_em = models.DateTimeField('Data Criação', auto_now_add=True)
    atualizado_em = models.DateTimeField('Última atuualização', auto_now=True)
    
    def __str__(self):
        return f'{self.texto} ({self.atualizado_em})'
