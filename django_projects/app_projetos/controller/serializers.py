from rest_framework import serializers
from .models import Projeto, Equipe


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
