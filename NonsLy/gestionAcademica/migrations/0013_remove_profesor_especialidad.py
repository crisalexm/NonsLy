# Generated by Django 4.1.3 on 2022-11-27 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionAcademica', '0012_curso_annio_academico'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profesor',
            name='especialidad',
        ),
    ]