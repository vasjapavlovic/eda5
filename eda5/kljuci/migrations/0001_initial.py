# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '0001_initial'),
        ('arhiv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kljuc',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=50)),
                ('vrsta_kljuca', models.IntegerField(choices=[(1, 'ključ'), (2, 'daljinec')])),
                ('status_kljuca', models.IntegerField(default=1, choices=[(1, 'za uporabo'), (2, 'odpisan')])),
                ('opomba_statusa_kljuca', models.CharField(blank=True, max_length=255, null=True, verbose_name='opomba spremembe statusa ključa')),
            ],
            options={
                'verbose_name_plural': 'ključi',
                'verbose_name': 'ključ',
            },
        ),
        migrations.CreateModel(
            name='PredajaKljuca',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('vrsta_predaje', models.IntegerField(choices=[(1, 'predaja'), (2, 'vračilo')])),
                ('predaja_datum', models.DateField()),
                ('vracilo_datum', models.DateField(blank=True, null=True)),
                ('vracilo_posebnosti', models.CharField(blank=True, max_length=255, null=True)),
                ('kljuc', models.ForeignKey(verbose_name='ključ', to='kljuci.Kljuc')),
                ('predaja_zapisnik', models.ForeignKey(related_name='predaja_zapisnik', null=True, blank=True, to='arhiv.Arhiviranje')),
                ('vracilo_zapisnik', models.ForeignKey(related_name='vracilo_zapisnik', null=True, blank=True, to='arhiv.Arhiviranje')),
                ('zahtevek', models.ForeignKey(null=True, blank=True, to='zahtevki.Zahtevek')),
            ],
            options={
                'verbose_name_plural': 'predaje kljucev',
                'verbose_name': 'predaja kljuca',
            },
        ),
        migrations.CreateModel(
            name='SklopKljucev',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=50, unique=True)),
                ('naziv', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'sklopi ključev',
                'verbose_name': 'sklop ključev',
            },
        ),
        migrations.AddField(
            model_name='kljuc',
            name='sklop_kljucev',
            field=models.ForeignKey(verbose_name='sklop ključev', to='kljuci.SklopKljucev'),
        ),
    ]
