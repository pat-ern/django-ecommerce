# Generated by Django 4.0.4 on 2022-05-30 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_persona_alter_categoria_idcategoria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='dv',
            field=models.CharField(max_length=1),
        ),
    ]
