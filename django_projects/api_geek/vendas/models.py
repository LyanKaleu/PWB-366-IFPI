from django.db import models
from produtos.models import Produto
from usuarios.models import Usuario


class Venda(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'tipo_usuario': 'CLIENTE'})
    produtos = models.ManyToManyField(Produto, through='ItemVenda')
    data_venda = models.DateTimeField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Venda {self.id} - Cliente: {self.cliente}"
    
    def save(self, *args, **kwargs):
        if self.cliente.tipo_usuario != 'CLIENTE':
            raise ValueError("Somente usuários do tipo 'cliente' podem realizar compras.")
        super().save(*args, **kwargs)
    

class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, related_name='itens', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.produto.quantidade_estoque < self.quantidade:
            raise ValueError(f"Estoque insuficiente para {self.produto.nome}.")
        if not self.preco_unitario:
            self.preco_unitario = self.produto.preco
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Venda {self.venda.id} - {self.quantidade}x {self.produto.nome} - R$ {self.preco_unitario:.2f}"
