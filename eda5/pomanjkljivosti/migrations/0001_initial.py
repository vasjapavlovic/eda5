# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0002_auto_20180104_1543'),
        ('zahtevki', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pomanjkljivost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_likvidiran', models.BooleanField(default=False)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('prioriteta', models.IntegerField(default=1, choices=[(0, 'Nizka prioriteta'), (1, 'Normalna'), (2, 'Velika prioriteta - Nujno')])),
                ('oznaka', models.CharField(max_length=20)),
                ('opis_text', models.TextField(verbose_name='Problem', null=True, blank=True)),
                ('ugotovljeno_dne', models.DateField(verbose_name='datum ugotovitve')),
                ('prijavil_text', models.CharField(verbose_name='prijavil', max_length=255)),
                ('element_text', models.CharField(verbose_name='element opisno', max_length=255, null=True, blank=True)),
                ('etaza_text', models.CharField(verbose_name='etaža opisno', max_length=50, null=True, blank=True)),
                ('lokacija_text', models.CharField(verbose_name='lokacija opisno', max_length=255, null=True, blank=True)),
                ('naziv', models.CharField(verbose_name='naziv pomanjkljivosti', max_length=255, null=True, blank=True)),
                ('opis', models.TextField(verbose_name='opis pomanjkljivosti', null=True, blank=True)),
                ('element', models.ManyToManyField(verbose_name='element', to='deli.ProjektnoMesto', blank=True)),
                ('zahtevek', models.ForeignKey(null=True, blank=True, verbose_name='zahtevek', to='zahtevki.Zahtevek')),
            ],
            options={
                'verbose_name': 'pomanjkljivost',
                'verbose_name_plural': 'pomanjkljivosti',
            },
        ),
    ]
