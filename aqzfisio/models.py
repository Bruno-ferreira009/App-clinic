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
        ("M", "Masculino"),
        ("F", "Feminino"),
        ("O", "Outros"),
        ("N", "Prefiro não informar")
    )

    sexo = models.CharField(max_length=9, choices=SEXO, )
    nome = models.CharField(max_length=100)
    cpf = models.IntegerField(unique=True)
    email = models.EmailField(blank=False, max_length=100, )
    celular = models.CharField(max_length=30)
    ativo = models.BooleanField()

    def __str__(self):
        return self.nome


class Agenda(models.Model):
    HORARIOS = (
        ("07:00 AM", "07:00 ás 08:00"),
        ("08:00 AM", "08:00 ás 09:00"),
        ("09:00 AM", "09:00 ás 10:00"),
        ("10:00 AM", "10:00 ás 11:00"),
        ("11:00 AM", "11:00 ás 12:00",)
    )
    horario = models.CharField(max_length=10, choices=HORARIOS)
    DIA = (
        ("SEGUNDA", "segunda-feira"),
        ("TERCA", "terça-feira"),
        ("QUARTA", "quarta-feira"),
        ("QUINTA", "quinta-feira"),
        ("SEXTA", "sexta-feira"),
    )
    dia = models.CharField(max_length=20, choices=DIA)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    # dia = models.DateField(help_text="Insira uma data para agenda", validators=[validar_dia])

    def __str__(self):
        return self.dia
