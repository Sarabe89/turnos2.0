# Generated by Django 4.2.7 on 2023-12-06 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0005_turno_status_alter_turno_fecha_alter_turno_hora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turno',
            name='status',
            field=models.CharField(choices=[('E', 'En Espera'), ('P', 'Atendiendo'), ('A', 'Ausente'), ('L', 'Atendido')], default='E', max_length=1, verbose_name='estado'),
        ),
    ]
