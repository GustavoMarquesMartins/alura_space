# Generated by Django 4.1 on 2024-01-04 05:55

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0012_alter_fotografia_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='foto',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='alura_space_fotografia'),
        ),
    ]
