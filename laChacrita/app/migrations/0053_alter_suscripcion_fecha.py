# Generated by Django 4.0.4 on 2022-06-27 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0052_alter_historialestadopedido_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suscripcion',
            name='fecha',
            field=models.DateField(auto_now=True),
        ),
    ]