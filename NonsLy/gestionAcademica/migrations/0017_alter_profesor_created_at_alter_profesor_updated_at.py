# Generated by Django 4.1.3 on 2022-11-28 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionAcademica', '0016_alter_profesor_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesor',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
