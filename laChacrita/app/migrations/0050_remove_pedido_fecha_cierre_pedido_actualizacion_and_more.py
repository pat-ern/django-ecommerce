# Generated by Django 4.0.4 on 2022-06-27 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0049_alter_calificacion_fecha_alter_contacto_fecha_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='fecha_cierre',
        ),
        migrations.AddField(
            model_name='pedido',
            name='actualizacion',
            field=models.DateTimeField(null=True),
        ),
        migrations.DeleteModel(
            name='CambioEstadoPedido',
        ),
    ]
