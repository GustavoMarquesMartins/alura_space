# Generated by Django 4.1 on 2024-01-09 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0014_remove_fotografia_foto_fotografia_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='imagem',
            field=models.FileField(blank=True, upload_to='imagens/'),
        ),
    ]