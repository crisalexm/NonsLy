# Generated by Django 4.1.3 on 2022-11-24 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colegio',
            fields=[
                ('col_id', models.AutoField(primary_key=True, serialize=False)),
                ('rbd', models.IntegerField()),
                ('nombre', models.CharField(help_text='Ingrese nombre del colegio.', max_length=50)),
                ('sigla', models.CharField(blank=True, max_length=5, null=True)),
                ('direccion', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'colegios',
                'db_table': 'colegio',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('prof_id', models.AutoField(primary_key=True, serialize=False)),
                ('rut', models.CharField(max_length=10, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido1', models.CharField(max_length=50)),
                ('apellido2', models.CharField(blank=True, max_length=50, null=True)),
                ('fechanacimiento', models.DateField(db_column='fechaNacimiento')),
                ('telefono', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=200, unique=True)),
                ('genero', models.CharField(max_length=10)),
                ('especialidad', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('colegio', models.ManyToManyField(max_length=50, to='gestionAcademica.colegio')),
            ],
            options={
                'verbose_name_plural': 'profesores',
                'db_table': 'profesor',
                'ordering': ['created_at'],
            },
        ),
    ]