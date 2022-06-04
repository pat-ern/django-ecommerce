# Generated by Django 4.0.4 on 2022-06-04 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_delete_snippet_alter_producto_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FiltroPrecios',
        ),
        migrations.AlterField(
            model_name='calificacion',
            name='fecha',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='calificacion',
            name='idProducto',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='calificacion',
            name='puntuacion',
            field=models.IntegerField(choices=[[0, '1'], [1, '2'], [2, '3'], [3, '4'], [4, '5']]),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fechaRegistro',
            field=models.DateField(auto_now_add=True),
        ),
    ]
