# Generated by Django 4.1.1 on 2022-09-29 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_rename_nombre_mascota_nombrem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citas',
            name='Fecha',
            field=models.DateField(max_length=100),
        ),
        migrations.AlterField(
            model_name='citas',
            name='Hora',
            field=models.DateField(max_length=100),
        ),
    ]
