# Generated by Django 4.1.4 on 2022-12-16 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aqzfisio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agenda',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='aqzfisio.cliente'),
            preserve_default=False,
        ),
    ]
