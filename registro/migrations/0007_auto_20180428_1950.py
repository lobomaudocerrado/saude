# Generated by Django 2.0.4 on 2018-04-28 22:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0006_auto_20180428_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peso',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 28, 19, 50, 16, 927311), verbose_name='Data da Pesagem'),
        ),
    ]
