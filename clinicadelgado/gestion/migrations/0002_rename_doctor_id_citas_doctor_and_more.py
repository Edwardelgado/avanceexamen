# Generated by Django 4.2.1 on 2023-06-03 01:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='citas',
            old_name='doctor_id',
            new_name='doctor',
        ),
        migrations.RenameField(
            model_name='citas',
            old_name='especialidad_id',
            new_name='especialidad',
        ),
        migrations.RenameField(
            model_name='citas',
            old_name='paciente_id',
            new_name='paciente',
        ),
    ]
