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
        fields = ['id', 'sexo', 'nome', 'matricula', 'email', 'celular', 'ativo']

    def validate_matricula(self, matricula):
        if len(matricula) != 11:
            raise serializers.ValidationError("A matricula deve conter 11 dígitos")
        return matricula

    def validate_nome(self, nome):
        if not nome.isalpha():
            raise serializers.ValidationError("Não inclua números neste campo")
        return nome
    def validate_celular(self, celular):
        if len(celular) < 11:
            raise serializers.ValidationError("O celular deve conter 11 dígitos")
        return celular


class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = ['horario', 'dia', 'cliente']
