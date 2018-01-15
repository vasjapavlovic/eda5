# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0003_remove_projektnomesto_tip_elementa'),
        ('planiranje', '0002_planiranoopravilo_aktivnost'),
        ('kontrolnilist', '0015_auto_20180111_1444'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanAktivnost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oznaka', models.CharField(null=True, blank=True, max_length=100)),
                ('oznaka_gen', models.CharField(null=True, blank=True, max_length=100)),
                ('naziv', models.CharField(null=True, blank=True, max_length=255)),
                ('opis', models.TextField(null=True, blank=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('planirano_opravilo', models.ForeignKey(to='planiranje.PlaniranoOpravilo', verbose_name='planirano opravilo')),
                ('projektno_mesto', models.ManyToManyField(blank=True, to='deli.ProjektnoMesto', verbose_name='projektno mesto')),
            ],
            options={
                'verbose_name_plural': 'Planirane Aktivnosti',
                'ordering': ('oznaka',),
                'verbose_name': 'Planirana Aktivnost',
            },
        ),
        migrations.CreateModel(
            name='PlanKontrolaSpecifikacija',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oznaka', models.CharField(null=True, blank=True, max_length=100)),
                ('oznaka_gen', models.CharField(null=True, blank=True, max_length=100)),
                ('naziv', models.CharField(null=True, blank=True, max_length=255)),
                ('opis', models.TextField(null=True, blank=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('vrednost_vrsta', models.IntegerField(choices=[(1, 'check'), (2, 'text'), (3, 'select')], default=1, verbose_name='vrsta vrednosti')),
                ('plan_aktivnost', models.ForeignKey(to='kontrolnilist.PlanAktivnost', verbose_name='planirana aktivnost')),
            ],
            options={
                'ordering': ['oznaka'],
            },
        ),
    ]
