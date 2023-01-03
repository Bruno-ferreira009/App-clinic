from rest_framework import serializers
from aqzfisio.models import Aplicativo, Especialidade, Cliente, Agenda
from aqzfisio.validators import *


class AplicativoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aplicativo
        fields = ['nome', 'descricao']


class EspecialidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidade
        fields = ['especialidade', 'data_criacao', 'data_modificacao']


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'sexo', 'nome', 'cpf', 'email', 'celular', 'ativo']

    def validate(self, data):
        if cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': "O cpf deve conter 11 dígitos"})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome': "Não inclua números neste campo"})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular': "O número de celular deve seguir este modelo: 11 45745-4578"})
        return data


class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = ['horario', 'dia', 'cliente']
        depth = 1
