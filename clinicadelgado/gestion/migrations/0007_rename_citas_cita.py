# Generated by Django 4.2.1 on 2023-06-04 05:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gestion', '0006_alter_doctor_doctor_direccion'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Citas',
            new_name='Cita',
        ),
    ]
