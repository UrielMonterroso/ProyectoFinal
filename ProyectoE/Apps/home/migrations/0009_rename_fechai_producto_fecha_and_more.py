# Generated by Django 4.1.1 on 2022-09-29 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_citas_hora'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='fechaI',
            new_name='fecha',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='nombreP',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='nombreProv',
            new_name='proveedor',
        ),
    ]
