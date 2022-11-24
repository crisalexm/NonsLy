# Generated by Django 4.1.3 on 2022-11-24 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionAcademica', '0002_alumno'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alumno',
            options={'ordering': ['created_at'], 'verbose_name_plural': 'alumnos'},
        ),
        migrations.RenameField(
            model_name='alumno',
            old_name='fechanacimiento',
            new_name='fecha_nacimiento',
        ),
        migrations.CreateModel(
            name='Apoderado',
            fields=[
                ('apo_id', models.AutoField(primary_key=True, serialize=False)),
                ('rut', models.CharField(max_length=10, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido1', models.CharField(max_length=50)),
                ('apellido2', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_nacimiento', models.DateField(db_column='fechaNacimiento')),
                ('telefono', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=200, unique=True)),
                ('genero', models.CharField(db_collation='utf8mb3_general_ci', max_length=10)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('alumno', models.ManyToManyField(to='gestionAcademica.alumno')),
            ],
            options={
                'verbose_name_plural': 'apoderados',
                'db_table': 'apoderado',
                'ordering': ['created_at'],
            },
        ),
    ]