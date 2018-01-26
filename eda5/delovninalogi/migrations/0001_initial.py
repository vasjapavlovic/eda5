# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Delo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('datum', models.DateField(blank=True, null=True)),
                ('time_start', models.DurationField(blank=True, null=True, verbose_name='Ura:Začeto')),
                ('time_stop', models.DurationField(blank=True, null=True, verbose_name='Ura:Končano')),
                ('delo_cas_rac', models.DecimalField(blank=True, max_digits=5, decimal_places=2, null=True, verbose_name='Porabljen čas [UR]')),
            ],
            options={
                'verbose_name_plural': 'Dela',
                'verbose_name': 'Delo',
            },
        ),
        migrations.CreateModel(
            name='DelovniNalog',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('datum_plan', models.DateField(blank=True, null=True, verbose_name='V planu za dne')),
                ('datum_start', models.DateField(blank=True, null=True, verbose_name='Začeto dne')),
                ('datum_stop', models.DateField(blank=True, null=True, verbose_name='Končano dne')),
            ],
            options={
                'verbose_name_plural': 'Delovni Nalogi',
                'verbose_name': 'Delovni Nalog',
            },
        ),
        migrations.CreateModel(
            name='DeloVrsta',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=20, unique=True)),
                ('naziv', models.CharField(max_length=255)),
                ('zap_st', models.IntegerField(default=99)),
                ('cena', models.DecimalField(max_digits=4, decimal_places=2)),
                ('stopnja_ddv', models.DecimalField(max_digits=4, decimal_places=3)),
            ],
            options={
                'verbose_name_plural': 'vrste del',
                'verbose_name': 'vrsta dela',
            },
        ),
        migrations.CreateModel(
            name='DeloVrstaSklop',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=20, unique=True)),
                ('naziv', models.CharField(max_length=255)),
                ('zap_st', models.IntegerField(default=99)),
            ],
            options={
                'verbose_name_plural': 'sklopi vrst del',
                'verbose_name': 'sklop vrst del',
            },
        ),
        migrations.CreateModel(
            name='Opravilo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('rok_izvedbe', models.DateField()),
                ('is_potrjen', models.BooleanField(default=False, verbose_name='Potrjeno iz strani nadzornika')),
                ('zmin', models.IntegerField(verbose_name='zaokrožitev [min]', default=15)),
            ],
            options={
                'verbose_name_plural': 'Opravila',
                'verbose_name': 'Opravilo',
            },
        ),
        migrations.CreateModel(
            name='VzorecOpravila',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('oznaka', models.CharField(blank=True, max_length=100, null=True)),
                ('oznaka_gen', models.CharField(blank=True, max_length=100, null=True)),
                ('naziv', models.CharField(blank=True, max_length=255, null=True)),
                ('opis', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('rok_izvedbe', models.DateField(blank=True, null=True)),
                ('is_potrjen', models.BooleanField(default=False, verbose_name='Potrjeno s strani nadzornika')),
            ],
            options={
                'verbose_name_plural': 'vzorci opravil',
                'verbose_name': 'vzorec opravila',
            },
        ),
    ]
