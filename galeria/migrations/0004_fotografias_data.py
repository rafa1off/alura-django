# Generated by Django 4.2 on 2023-04-19 23:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0003_fotografias_publicada'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografias',
            name='data',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
