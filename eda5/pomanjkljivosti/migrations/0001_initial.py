# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '__first__'),
        ('deli', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pomanjkljivost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_likvidiran', models.BooleanField(default=False)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano')])),
                ('prioriteta', models.IntegerField(default=1, choices=[(0, 'Nizka prioriteta'), (1, 'Normalna'), (2, 'Velika prioriteta - Nujno')])),
                ('oznaka', models.CharField(max_length=20)),
                ('opis_text', models.TextField(blank=True, verbose_name='Problem', null=True)),
                ('ugotovljeno_dne', models.DateField(verbose_name='datum ugotovitve')),
                ('prijavil_text', models.CharField(verbose_name='prijavil', max_length=255)),
                ('element_text', models.CharField(blank=True, verbose_name='element opisno', null=True, max_length=255)),
                ('etaza_text', models.CharField(blank=True, verbose_name='etaža opisno', null=True, max_length=50)),
                ('lokacija_text', models.CharField(blank=True, verbose_name='lokacija opisno', null=True, max_length=255)),
                ('naziv', models.CharField(blank=True, verbose_name='naziv pomanjkljivosti', null=True, max_length=255)),
                ('opis', models.TextField(blank=True, verbose_name='opis pomanjkljivosti', null=True)),
                ('element', models.ManyToManyField(blank=True, verbose_name='element', to='deli.ProjektnoMesto')),
                ('zahtevek', models.ForeignKey(blank=True, null=True, verbose_name='zahtevek', to='zahtevki.Zahtevek')),
            ],
            options={
                'verbose_name_plural': 'pomanjkljivosti',
                'verbose_name': 'pomanjkljivost',
            },
        ),
    ]
