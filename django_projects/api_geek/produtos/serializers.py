from rest_framework import serializers
from .models import Produto, Categoria, Franquia


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class FranquiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Franquia
        fields = '__all__'


class ProdutoSerializer(serializers.ModelSerializer):
    categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all())
    franquia = serializers.PrimaryKeyRelatedField(queryset=Franquia.objects.all())

    class Meta:
        model = Produto
        fields = ['id', 'nome', 'descricao', 'preco', 'quantidade_estoque', 'categoria', 'franquia']

    def create(self, validated_data):
        categoria = validated_data.pop('categoria')
        franquia = validated_data.pop('franquia')

        categoria_obj, _ = Categoria.objects.get_or_create(id=categoria.id)
        franquia_obj, _ = Franquia.objects.get_or_create(id=franquia.id)

        produto = Produto.objects.create(categoria=categoria_obj, franquia=franquia_obj, **validated_data)
        return produto
    
    def validate_preco(self, preco):
        if preco < 0:
            raise serializers.ValidationError("O preço não pode ser negativo.")
        return preco
    
    def validate_quantidade_estoque(self, quantidade_estoque):
        if quantidade_estoque < 0:
            raise serializers.ValidationError("A quantidade em estoque não pode ser negativa.")
        return quantidade_estoque
    

class ReporEstoqueSerializer(serializers.ModelSerializer):
    quantidade = serializers.IntegerField(required=True, min_value=1)

    class Meta:
        model = Produto
        fields = ['quantidade']
