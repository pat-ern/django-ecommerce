# Generated by Django 4.0.4 on 2022-06-04 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_alter_contacto_correo_alter_donacion_correo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donacion',
            name='tipoDonacion',
        ),
    ]