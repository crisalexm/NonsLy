# Generated by Django 4.1.3 on 2022-12-10 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionAcademica', '0040_nota_nota_obtenida2_nota_nota_obtenida3_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nota',
            old_name='alum',
            new_name='alumno',
        ),
        migrations.RenameField(
            model_name='nota',
            old_name='eva',
            new_name='evaluacion',
        ),
        migrations.RenameField(
            model_name='nota',
            old_name='prof',
            new_name='profesor',
        ),
    ]
