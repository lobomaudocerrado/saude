# Generated by Django 2.0.4 on 2018-04-28 22:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0005_auto_20180421_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peso',
            name='data',
            field=models.DateTimeField(default=datetime.date.today, verbose_name='Data da Pesagem'),
        ),
    ]
