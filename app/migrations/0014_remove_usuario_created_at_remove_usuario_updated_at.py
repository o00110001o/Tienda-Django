# Generated by Django 4.0.1 on 2023-01-21 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_planta_created_at_remove_planta_imagen_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='updated_at',
        ),
    ]