from rest_framework import serializers
from .models import Venda, ItemVenda
from produtos.models import Produto


class ItemVendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemVenda
        fields = ['produto', 'quantidade', 'preco_unitario']
        extra_kwargs = {
            'preco_unitario': {'read_only': True}
        }

    def validate(self, data):
        produto = data['produto']
        quantidade = data['quantidade']

        if produto.quantidade_estoque < quantidade:
            raise serializers.ValidationError(
                f'Estoque insuficiente para o produto {produto.nome}'
                f'Estoque disponível: {produto.quantidade_estoque}'
            )
        
        if produto.preco is None:
            raise serializers.ValidationError(f'O preço do produto {produto.nome} não está definido.')

        return data


class VendaSerializer(serializers.ModelSerializer):
    itens = ItemVendaSerializer(many=True)

    class Meta:
        model = Venda
        fields = ['cliente', 'itens', 'valor_total', 'data_venda']
        read_only_fields = ['valor_total', 'data_venda']

    def validate_itens(self, value):
        for item in value:
            produto = item['produto']
            quantidade = item['quantidade']

            if produto.quantidade_estoque < quantidade:
                raise serializers.ValidationError(
                    f'Estoque insuficiente para o produto {produto.nome}'
                    f'Estoque disponível: {produto.quantidade_estoque}'
                )
        
        return value
    

    def create(self, validated_data):
        itens_data = validated_data.pop('itens')
        venda = Venda.objects.create(**validated_data)

        valor_total = 0
        for item_data in itens_data:
            produto = item_data['produto']
            quantidade = item_data['quantidade']
            
            preco_unitario = produto.preco

            produto.quantidade_estoque -= quantidade
            produto.save()

            ItemVenda.objects.create(
                venda=venda,
                produto=produto,
                quantidade=quantidade,
                preco_unitario=preco_unitario
            )

            valor_total += quantidade * preco_unitario
        
        venda.valor_total = valor_total
        venda.save()

        return venda
