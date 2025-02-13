from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
    

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    criado_em = models.DateTimeField(auto_now_add=True)
    produtos = models.ManyToManyField(Cliente, through='Pedido', related_name='produtos') 

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cliente} - {self.produto}'
