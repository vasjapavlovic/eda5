# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.IntegerField(choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno')], default=0)),
                ('datum', models.DateField(null=True, blank=True)),
                ('time_start', models.DurationField(verbose_name='Ura:Začeto', null=True, blank=True)),
                ('time_stop', models.DurationField(verbose_name='Ura:Končano', null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Delo',
                'verbose_name_plural': 'Dela',
            },
        ),
        migrations.CreateModel(
            name='DelovniNalog',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.IntegerField(choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno')], default=0)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('datum_plan', models.DateField(verbose_name='V planu za dne', null=True, blank=True)),
                ('datum_start', models.DateField(verbose_name='Začeto dne', null=True, blank=True)),
                ('datum_stop', models.DateField(verbose_name='Končano dne', null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Delovni Nalog',
                'verbose_name_plural': 'Delovni Nalogi',
            },
        ),
        migrations.CreateModel(
            name='DeloVrsta',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('zap_st', models.IntegerField(default=99)),
                ('cena', models.DecimalField(max_digits=4, decimal_places=2)),
                ('stopnja_ddv', models.DecimalField(max_digits=4, decimal_places=3)),
            ],
            options={
                'verbose_name': 'vrsta dela',
                'verbose_name_plural': 'vrste del',
            },
        ),
        migrations.CreateModel(
            name='DeloVrstaSklop',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('zap_st', models.IntegerField(default=99)),
            ],
            options={
                'verbose_name': 'sklop vrst del',
                'verbose_name_plural': 'sklopi vrst del',
            },
        ),
        migrations.CreateModel(
            name='Opravilo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('rok_izvedbe', models.DateField()),
                ('is_potrjen', models.BooleanField(verbose_name='Potrjeno iz strani nadzornika', default=False)),
                ('element', models.ManyToManyField(to='deli.Element')),
            ],
            options={
                'verbose_name': 'Opravilo',
                'verbose_name_plural': 'Opravila',
            },
        ),
    ]
