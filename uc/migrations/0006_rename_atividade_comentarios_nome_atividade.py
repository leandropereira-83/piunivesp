# Generated by Django 3.2.9 on 2021-11-22 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uc', '0005_comentarios'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentarios',
            old_name='atividade',
            new_name='nome_atividade',
        ),
    ]
