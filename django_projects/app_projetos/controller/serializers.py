from rest_framework import serializers
from .models import Projeto, Equipe, Comentario


class EquipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipe
        fields = '__all__'


class EquipeBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipe
        fields = ['id', 'nome']


class ProjetoSerializer(serializers.ModelSerializer):
    equipe = EquipeBasicSerializer()

    class Meta:
        model = Projeto
        fields = ['id', 'nome', 'descricao', 'data_inicio', 'data_final', 'descricao', 'equipe']
    
    def create(self, validated_data):
        equipe_data = validated_data.pop('equipe')
        equipe = Equipe.objects.create(**equipe_data)
        projeto = Projeto.objects.create(equipe=equipe, **validated_data)
        return projeto


class ProjetoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projeto
        fields = ['id', 'nome', 'data_inicio', 'data_final', 'orcamento']


class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'
        