# Generated by Django 2.0.4 on 2018-04-21 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0003_peso_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='slug',
            field=models.CharField(blank=True, max_length=100, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='peso',
            name='descricao',
            field=models.TextField(blank=True, verbose_name='Observações'),
        ),
    ]
