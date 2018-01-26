# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planiranje', '0001_initial'),
        ('deli', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('oznaka', models.CharField(blank=True, max_length=100, null=True)),
                ('oznaka_gen', models.CharField(blank=True, max_length=100, null=True)),
                ('naziv', models.CharField(blank=True, max_length=255, null=True)),
                ('opis', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('plan_kontrola_specifikacija', models.ForeignKey(verbose_name='poročilo o rezultatu kontrole', to='planiranje.PlanKontrolaSpecifikacija')),
                ('projektno_mesto', models.ForeignKey(verbose_name='projektno mesto', to='deli.ProjektnoMesto')),
            ],
            options={
                'verbose_name': 'Report maped PlanKontrolaSpeciikacija',
            },
        ),
    ]
