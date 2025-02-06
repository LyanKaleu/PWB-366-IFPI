from django.db import models
from django.contrib import admin
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import datetime


# Create your models here.
class Projeto(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    descricao = models.CharField('Descrição', max_length=200, blank=False, null=False)
    data_inicio = models.DateField('Data de Início')
    data_final = models.DateField('Data de Fim')
    orcamento = models.DecimalField('Orçamento', max_digits=10, decimal_places=2, blank=False, null=True)

    equipe = models.ForeignKey(
        'Equipe', 
        on_delete=models.CASCADE,
        related_name='projetos',
        null=True,
        blank=True
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
    ativa = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipes'
        ordering = ['nome']
    
    def __str__(self):
        return self.nome
    
    @admin.display(description='Qtd Membros')
    def quantidade_membros(self):
        return self.membros.count()


SEXO_CHOICES = (('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro'))
    

class Membro(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    sexo = models.CharField(max_length=1, default='O', choices=SEXO_CHOICES, blank=False, null=False)
    funcao = models.CharField(max_length=100, blank=False, null=False)
    telefone = models.CharField(
        max_length=15,
        help_text='(99) 99999-9999',
        validators=[RegexValidator(regex=r'^\(\d{2}\) \d{5}-\d{4}$', message='Telefone deve estar no formato (99) 99999-9999')],
        null=True,
        blank=True
    )
    ativo = models.BooleanField(default=True)
    equipe = models.ForeignKey( 
        'Equipe', 
        on_delete=models.CASCADE,
        related_name='membros',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Membro'
        verbose_name_plural = 'Membros'
        ordering = ['nome']

    def __str__(self):
        return f'{self.nome} ({self.equipe})'
    
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
        related_name='atividades',
        null=True,
        blank=True
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
