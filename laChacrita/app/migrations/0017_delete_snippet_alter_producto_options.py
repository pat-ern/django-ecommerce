# Generated by Django 4.0.4 on 2022-06-03 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_snippet'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Snippet',
        ),
        migrations.AlterModelOptions(
            name='producto',
            options={'ordering': ('nombre',)},
        ),
    ]
