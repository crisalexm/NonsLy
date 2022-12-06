# Generated by Django 4.1.3 on 2022-11-30 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionAcademica', '0023_alter_alumno_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='genero',
            field=models.CharField(choices=[('Masculino', 'Masculino'), ('INACTIVO', 'Femenino'), ('Otro', 'Otro')], db_collation='utf8mb3_general_ci', max_length=10),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='status',
            field=models.CharField(choices=[('ACTIVO', 'Activo'), ('INACTIVO', 'Inactivo')], db_collation='utf8mb3_general_ci', max_length=8),
        ),
    ]