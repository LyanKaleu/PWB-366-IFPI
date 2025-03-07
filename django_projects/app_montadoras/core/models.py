from django.contrib import admin
from django.db import models
import datetime


class Montadora(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=128, blank=False, null=False)
    pais = models.CharField(verbose_name='País', max_length=128, blank=False, null=False)
    ano_fundacao = models.PositiveIntegerField(verbose_name='Ano de Fundação')

    class Meta:
        verbose_name = 'Montadora'
        verbose_name_plural = 'Montadoras'
        ordering = ['nome']

    def __str__(self):
        return f'{self.nome} - {self.pais}'
    
    @admin.display(description='Anos de operação')
    def idade(self):
        return datetime.date.today().year - self.ano_fundacao

    @admin.display(description='Qtd Veículos')
    def quantidade_veiculos(self):
        return self.veiculos.count()
    

MOTOR_CHOICES = (
    ('1.0', 'Motor 1.0'),
    ('1.3', 'Motor 1.3'), 
    ('1.4', 'Motor 1.4'), 
    ('1.6', 'Motor 1.6'), 
    ('2.0', 'Motor 2.0')
)


class ModeloVeiculo(models.Model):
    nome = models.CharField(max_length=128, null=False, blank=False)
    motorizacao = models.CharField(max_length=5, choices=MOTOR_CHOICES, null=False, blank=False)
    em_producao = models.BooleanField(default=False, blank=False, null=False)

    # Relacionamento (Many-to-One)
    montadora = models.ForeignKey(Montadora, on_delete=models.RESTRICT, related_name='veiculos')

    class Meta:
        verbose_name = 'Modelo de Veículo'
        verbose_name_plural = 'Modelos de Veículos'
        ordering = ['montadora', 'nome']

    def __str__(self):
        return f'{self.montadora} - {self.nome}'


class Veiculos(models.Model):
    placa = models.CharField(max_length=7, null=False, blank=False)
    cor = models.CharField(max_length=32, null=False, blank=False)
    ano = models.PositiveIntegerField(null=False, blank=False)
    modelo = models.ForeignKey(ModeloVeiculo, on_delete=models.RESTRICT, related_name='veiculos')
    km_rodados = models.PositiveIntegerField(null=False, blank=False)

    class Meta:
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'
        ordering = ['modelo__montadora__nome', 'modelo__nome']

    def __str__(self):
        return f'{self.modelo} - {self.placa}'
