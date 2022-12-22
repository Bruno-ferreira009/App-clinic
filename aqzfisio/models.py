from django.db import models
from datetime import date


class Aplicativo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)


def __str__(self):
    return self.nome


class Especialidade(models.Model):
    especialidade = models.CharField(max_length=80)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.especialidade


class Cliente(models.Model):
    SEXO = (
        ("MAS", "Maculino"),
        ("FEM", "Feminino")
    )

    sexo = models.CharField(max_length=9, choices=SEXO, )
    nome = models.CharField(max_length=30)
    matricula = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=False, max_length=30, )
    celular = models.CharField(max_length=30)
    ativo = models.BooleanField()

    def __str__(self):
        return self.nome


class Agenda(models.Model):
    HORARIOS = (
        ("1", "07:00 ás 08:00"),
        ("2", "08:00 ás 09:00"),
        ("3", "09:00 ás 10:00"),
        ("4", "10:00 ás 11:00"),
        ("5", "11:00 ás 12:00"),
    )
    horario = models.CharField(max_length=10, choices=HORARIOS)
    DIA = (
        ("SEG", "segunda-feira"),
        ("TER", "terça-feira"),
        ("QUA", "quarta-feira"),
        ("QUI", "quinta-feira"),
        ("SEX", "sexta-feira"),
    )
    dia = models.CharField(max_length=20, choices=DIA)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.dia
