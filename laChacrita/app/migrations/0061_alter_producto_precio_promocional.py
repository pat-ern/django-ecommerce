# Generated by Django 4.0.4 on 2022-06-29 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0060_alter_promocion_descuento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio_promocional',
            field=models.IntegerField(default=models.IntegerField(null=True), null=True),
        ),
    ]