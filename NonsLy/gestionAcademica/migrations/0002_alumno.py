# Generated by Django 4.1.3 on 2022-11-24 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionAcademica', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('alum_id', models.AutoField(primary_key=True, serialize=False)),
                ('rut', models.CharField(max_length=10, unique=True)),
                ('nombre', models.CharField(db_collation='utf8mb3_general_ci', max_length=50)),
                ('apellido1', models.CharField(db_collation='utf8mb3_general_ci', max_length=50)),
                ('apellido2', models.CharField(blank=True, db_collation='utf8mb3_general_ci', max_length=50, null=True)),
                ('fechanacimiento', models.DateField(db_column='fechaNacimiento')),
                ('telefono', models.CharField(db_collation='utf8mb3_general_ci', max_length=11)),
                ('email', models.CharField(max_length=200, unique=True)),
                ('genero', models.CharField(db_collation='utf8mb3_general_ci', max_length=10)),
                ('status', models.CharField(db_collation='utf8mb3_general_ci', max_length=8)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('colegio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestionAcademica.colegio')),
            ],
            options={
                'verbose_name_plural': 'profesores',
                'db_table': 'alumno',
                'ordering': ['created_at'],
            },
        ),
    ]