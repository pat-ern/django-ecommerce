# Generated by Django 4.0.4 on 2022-06-05 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_alter_donacion_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donacion',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]
