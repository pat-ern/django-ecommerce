# Generated by Django 4.0.4 on 2022-06-22 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0037_alter_calificacion_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calificacion',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario'),
        ),
    ]
