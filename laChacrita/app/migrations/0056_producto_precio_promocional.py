# Generated by Django 4.0.4 on 2022-06-29 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0055_promocion_producto_promocion'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='precio_promocional',
            field=models.IntegerField(null=True),
        ),
    ]
