# Generated by Django 4.2.7 on 2023-12-06 14:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0004_alter_turno_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='turno',
            name='status',
            field=models.CharField(choices=[('E', 'En Espera'), ('P', 'Atendiendo'), ('A', 'Ausente')], default='E', max_length=1),
        ),
        migrations.AlterField(
            model_name='turno',
            name='fecha',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='turno',
            name='hora',
            field=models.TimeField(default='07:00'),
        ),
    ]
