# Generated by Django 4.0.1 on 2023-01-21 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_planta_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planta',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='planta',
            name='imagen',
        ),
        migrations.RemoveField(
            model_name='planta',
            name='stock',
        ),
        migrations.RemoveField(
            model_name='planta',
            name='updated_at',
        ),
    ]
