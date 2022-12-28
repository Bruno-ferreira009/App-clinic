# Generated by Django 4.1.4 on 2022-12-28 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aplicativo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.CharField(choices=[('M', 'Maculino'), ('F', 'Feminino')], max_length=9)),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.IntegerField(unique=True)),
                ('email', models.EmailField(max_length=100)),
                ('celular', models.CharField(max_length=30)),
                ('ativo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Especialidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especialidade', models.CharField(max_length=80)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_modificacao', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.CharField(choices=[('07:00 AM', '07:00 ás 08:00'), ('08:00 AM', '08:00 ás 09:00'), ('09:00 AM', '09:00 ás 10:00'), ('10:00 AM', '10:00 ás 11:00'), ('11:00 AM', '11:00 ás 12:00')], max_length=10)),
                ('dia', models.CharField(choices=[('SEGUNDA', 'segunda-feira'), ('TERCA', 'terça-feira'), ('QUARTA', 'quarta-feira'), ('QUINTA', 'quinta-feira'), ('SEXTA', 'sexta-feira')], max_length=20)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aqzfisio.cliente')),
            ],
        ),
    ]
