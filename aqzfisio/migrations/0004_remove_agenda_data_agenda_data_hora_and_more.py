# Generated by Django 4.1.4 on 2022-12-26 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aqzfisio', '0003_agenda_data_alter_agenda_dia_alter_cliente_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agenda',
            name='data',
        ),
        migrations.AddField(
            model_name='agenda',
            name='data_hora',
            field=models.DateTimeField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='agenda',
            name='horario',
            field=models.CharField(choices=[('07:00 AM', '07:00 ás 08:00'), ('08:00 AM', '08:00 ás 09:00'), ('09:00 AM', '09:00 ás 10:00'), ('10:00 AM', '10:00 ás 11:00'), ('11:00 AM', '11:00 ás 12:00')], max_length=10),
        ),
    ]
