# Generated by Django 3.2.9 on 2021-11-24 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0002_auto_20211123_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='uc',
            name='obs_docente',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]