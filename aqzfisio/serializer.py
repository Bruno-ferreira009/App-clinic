from rest_framework import serializers
from aqzfisio.models import Aplicativo, Especialidade, Cliente, Agenda


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
        fields = ['sexo', 'nome', 'matricula', 'email', 'celular', 'ativo']


class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = '__all__'
