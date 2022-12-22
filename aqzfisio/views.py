from rest_framework import viewsets
from aqzfisio.models import *
from aqzfisio.serializer import AplicativoSerializer, EspecialidadeSerializer, ClienteSerializer, AgendaSerializer


class AplicativoViewSet(viewsets.ModelViewSet):
    """Exibindo o Aplicativo"""
    queryset = Aplicativo.objects.all()
    serializer_class = AplicativoSerializer


class EspecialidadeViewSet(viewsets.ModelViewSet):
    """Exibindo a Especialidade"""
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    """Exibindo Clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class AgendaViewSet(viewsets.ModelViewSet):
    """Exibindo a Agenda"""
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer


