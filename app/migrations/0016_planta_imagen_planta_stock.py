# Generated by Django 4.0.5 on 2023-01-22 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_remove_planta_codigo_planta_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='planta',
            name='imagen',
            field=models.ImageField(null=True, upload_to='productos'),
        ),
        migrations.AddField(
            model_name='planta',
            name='stock',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
