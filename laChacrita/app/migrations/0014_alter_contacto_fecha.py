# Generated by Django 4.0.4 on 2022-06-02 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_rename_texto_contacto_mensaje_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='fecha',
            field=models.DateField(auto_now_add=True),
        ),
    ]