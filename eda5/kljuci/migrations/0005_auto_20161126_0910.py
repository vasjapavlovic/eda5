# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lastnistvo', '0013_auto_20160102_1757'),
        ('kljuci', '0004_auto_20161124_2259'),
    ]

    operations = [
        migrations.CreateModel(
            name='PredajaKljuca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datum_predaje', models.DateField()),
                ('kljuc', models.ForeignKey(to='kljuci.Kljuc', verbose_name='ključ')),
                ('predaja_lastnine', models.ForeignKey(to='lastnistvo.PredajaLastnine', blank=True, null=True)),
            ],
            options={
                'verbose_name': 'predaja kljuca',
                'verbose_name_plural': 'predaje kljucev',
            },
        ),
        migrations.RemoveField(
            model_name='predajakljucev',
            name='kljuc',
        ),
        migrations.RemoveField(
            model_name='predajakljucev',
            name='predaja_lastnine',
        ),
        migrations.DeleteModel(
            name='PredajaKljucev',
        ),
    ]
