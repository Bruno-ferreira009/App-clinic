from rest_framework import viewsets, status
from rest_framework.response import Response
from django.http.response import JsonResponse

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

    def create(self, request, *args, **kwargs):
        cliente = Cliente.objects.get(cliente=request.data['cliente']['id'])
        agenda = Agenda.objects.create(
            horario=request.data['horario'],
            dia=request.data['dia'],
            cliente=cliente
        )

        agenda = AgendaSerializer(agenda)

        return Response(agenda.data)
