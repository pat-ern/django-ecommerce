# Generated by Django 4.0.4 on 2022-06-17 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_tiposuscripcion_monto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='suscripcion',
            old_name='tipoSuscripcion',
            new_name='tipo_suscripcion',
        ),
        migrations.RemoveField(
            model_name='suscripcion',
            name='monto',
        ),
        migrations.AlterField(
            model_name='tiposuscripcion',
            name='monto',
            field=models.IntegerField(default=0, verbose_name='Monto de suscripcion'),
        ),
    ]
