from django.contrib import admin
from aqzfisio.models import Aplicativo, Especialidade, Cliente, Agenda


class Aplicativos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao',)
    list_display_links = ('id', 'nome',)


admin.site.register(Aplicativo, Aplicativos)


class Especialidades(admin.ModelAdmin):
    list_display = ('id', 'especialidade', 'data_criacao')
    search_fields = ('id', 'especialidade',)


admin.site.register(Especialidade, Especialidades)


class Clientes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'email', 'celular')
    list_display_links = ('id', 'nome')
    search_fields = ('id', 'nome', 'cpf')
    list_per_page = 10


admin.site.register(Cliente, Clientes)


class Agendas(admin.ModelAdmin):
    list_display = ('id', 'horario', 'dia')
    list_display_links = ('id', 'dia')


admin.site.register(Agenda, Agendas)
