# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '0001_initial'),
        ('deli', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pomanjkljivost',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_likvidiran', models.BooleanField(default=False)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('prioriteta', models.IntegerField(default=1, choices=[(0, 'Nizka prioriteta'), (1, 'Normalna'), (2, 'Velika prioriteta - Nujno')])),
                ('oznaka', models.CharField(max_length=20)),
                ('opis_text', models.TextField(blank=True, null=True, verbose_name='Problem')),
                ('ugotovljeno_dne', models.DateField(verbose_name='datum ugotovitve')),
                ('prijavil_text', models.CharField(verbose_name='prijavil', max_length=255)),
                ('element_text', models.CharField(blank=True, max_length=255, null=True, verbose_name='element opisno')),
                ('etaza_text', models.CharField(blank=True, max_length=50, null=True, verbose_name='etaža opisno')),
                ('lokacija_text', models.CharField(blank=True, max_length=255, null=True, verbose_name='lokacija opisno')),
                ('naziv', models.CharField(blank=True, max_length=255, null=True, verbose_name='naziv pomanjkljivosti')),
                ('opis', models.TextField(blank=True, null=True, verbose_name='opis pomanjkljivosti')),
                ('element', models.ManyToManyField(blank=True, to='deli.ProjektnoMesto', verbose_name='element')),
                ('zahtevek', models.ForeignKey(null=True, verbose_name='zahtevek', blank=True, to='zahtevki.Zahtevek')),
            ],
            options={
                'verbose_name_plural': 'pomanjkljivosti',
                'verbose_name': 'pomanjkljivost',
            },
        ),
    ]
