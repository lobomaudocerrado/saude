# Generated by Django 2.0.4 on 2018-04-13 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='Peso')),
                ('data', models.DateTimeField(verbose_name='até')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.Pessoa', verbose_name='Pessoa')),
            ],
            options={
                'ordering': ['-data'],
                'verbose_name_plural': 'Metas',
                'verbose_name': 'Meta',
            },
        ),
    ]
