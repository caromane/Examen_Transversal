# Generated by Django 3.2.5 on 2021-07-11 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mecanicos', '0002_contacto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacto',
            name='clave',
        ),
        migrations.AddField(
            model_name='contacto',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='contacto',
            name='mensaje',
            field=models.TextField(null=True),
        ),
    ]