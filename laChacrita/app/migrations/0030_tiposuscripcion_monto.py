# Generated by Django 4.0.4 on 2022-06-17 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_suscripcion_tiposuscripcion_delete_donacion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tiposuscripcion',
            name='monto',
            field=models.IntegerField(default=0),
        ),
    ]
