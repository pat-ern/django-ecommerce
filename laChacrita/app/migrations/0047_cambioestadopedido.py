# Generated by Django 4.0.4 on 2022-06-25 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0046_remove_suscripcion_correo_remove_suscripcion_nombre_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CambioEstadoPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('nuevo_estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.estadopedido')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pedido')),
            ],
        ),
    ]
