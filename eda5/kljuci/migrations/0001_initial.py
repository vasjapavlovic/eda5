# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lastnistvo', '0013_auto_20160102_1757'),
        ('deli', '0003_auto_20151229_1357'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kljuc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('oznaka', models.CharField(max_length=50)),
                ('vrsta_kljuca', models.IntegerField(choices=[(1, 'ključ'), (2, 'daljinec')])),
                ('status_kljuca', models.IntegerField(choices=[(1, 'za uporabo'), (2, 'odpisan')], default=1)),
            ],
            options={
                'verbose_name_plural': 'ključi',
                'verbose_name': 'ključ',
            },
        ),
        migrations.CreateModel(
            name='PredajaKljucev',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('datum_predaje_kljuca', models.DateField()),
                ('kljuc', models.ManyToManyField(to='kljuci.Kljuc')),
                ('predaja_lastnine', models.ForeignKey(to='lastnistvo.PredajaLastnine', blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'predaje kljucev',
                'verbose_name': 'predaja kljuca',
            },
        ),
        migrations.CreateModel(
            name='SklopKljucev',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('oznaka', models.CharField(unique=True, max_length=50)),
                ('naziv', models.CharField(max_length=255)),
                ('element', models.ForeignKey(to='deli.Element', blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'ključi',
                'verbose_name': 'ključ',
            },
        ),
        migrations.AddField(
            model_name='kljuc',
            name='sklop_kljucev',
            field=models.ForeignKey(to='kljuci.SklopKljucev', verbose_name='sklop ključev'),
        ),
    ]
