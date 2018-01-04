# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arhiv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kljuc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('oznaka', models.CharField(max_length=50)),
                ('vrsta_kljuca', models.IntegerField(choices=[(1, 'ključ'), (2, 'daljinec')])),
                ('status_kljuca', models.IntegerField(default=1, choices=[(1, 'za uporabo'), (2, 'odpisan')])),
                ('opomba_statusa_kljuca', models.CharField(verbose_name='opomba spremembe statusa ključa', max_length=255, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'ključ',
                'verbose_name_plural': 'ključi',
            },
        ),
        migrations.CreateModel(
            name='PredajaKljuca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('vrsta_predaje', models.IntegerField(choices=[(1, 'predaja'), (2, 'vračilo')])),
                ('predaja_datum', models.DateField()),
                ('vracilo_datum', models.DateField(null=True, blank=True)),
                ('vracilo_posebnosti', models.CharField(max_length=255, null=True, blank=True)),
                ('kljuc', models.ForeignKey(verbose_name='ključ', to='kljuci.Kljuc')),
                ('predaja_zapisnik', models.ForeignKey(null=True, blank=True, to='arhiv.Arhiviranje', related_name='predaja_zapisnik')),
                ('vracilo_zapisnik', models.ForeignKey(null=True, blank=True, to='arhiv.Arhiviranje', related_name='vracilo_zapisnik')),
            ],
            options={
                'verbose_name': 'predaja kljuca',
                'verbose_name_plural': 'predaje kljucev',
            },
        ),
        migrations.CreateModel(
            name='SklopKljucev',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('oznaka', models.CharField(max_length=50, unique=True)),
                ('naziv', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'sklop ključev',
                'verbose_name_plural': 'sklopi ključev',
            },
        ),
    ]
