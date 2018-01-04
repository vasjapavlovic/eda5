# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0001_initial'),
        ('deli', '0002_auto_20180104_1543'),
        ('zahtevki', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('oznaka', models.CharField(max_length=25)),
                ('naziv', models.CharField(max_length=255)),
                ('zap_st', models.IntegerField(verbose_name='zaporedna številka', default=0)),
                ('opis', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'plan',
                'verbose_name_plural': 'plani',
            },
        ),
        migrations.CreateModel(
            name='PlaniranaAktivnost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('naziv_opravila_izven_plana', models.CharField(max_length=255, blank=True)),
                ('artikel_plan', models.ForeignKey(null=True, blank=True, to='katalog.ArtikelPlan')),
                ('element', models.ForeignKey(null=True, blank=True, to='deli.Element')),
            ],
            options={
                'verbose_name': 'planirana aktivnost',
                'verbose_name_plural': 'planirane aktivnosti',
            },
        ),
        migrations.CreateModel(
            name='PlaniranoOpravilo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('oznaka', models.CharField(max_length=25)),
                ('naziv', models.CharField(max_length=255)),
                ('namen', models.CharField(max_length=255)),
                ('obseg', models.TextField()),
                ('perioda_predpisana_enota', models.CharField(verbose_name='enota periode', max_length=5, choices=[('dan', 'Dan'), ('teden', 'Teden'), ('mesec', 'Mesec'), ('leto', 'Leto')])),
                ('perioda_predpisana_enota_kolicina', models.IntegerField(verbose_name='kolicina enote periode')),
                ('perioda_predpisana_kolicina_na_enoto', models.IntegerField(verbose_name='kolicina na enoto periode')),
                ('datum_prve_izvedbe', models.DateField(null=True, blank=True)),
                ('datum_izvedeno_dne', models.DateField(verbose_name='Izvedeno dne', null=True, blank=True)),
                ('datum_naslednjega_opravila', models.DateField(verbose_name='Naslednji pregled', null=True, blank=True)),
                ('zmin', models.IntegerField(verbose_name='zaokrožitev [min]', default=15)),
                ('opomba', models.TextField(blank=True)),
                ('plan', models.ForeignKey(to='planiranje.Plan')),
            ],
            options={
                'verbose_name': 'planirano opravilo',
                'ordering': ('oznaka',),
                'verbose_name_plural': 'planirana opravila',
            },
        ),
        migrations.CreateModel(
            name='SkupinaPlanov',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('oznaka', models.CharField(max_length=25)),
                ('naziv', models.CharField(max_length=255)),
                ('zap_st', models.IntegerField(verbose_name='zaporedna številka', default=0)),
            ],
            options={
                'verbose_name': 'skupina planov',
                'ordering': ('zap_st',),
                'verbose_name_plural': 'skupine planov',
            },
        ),
        migrations.AddField(
            model_name='planiranaaktivnost',
            name='planirano_opravilo',
            field=models.ForeignKey(null=True, blank=True, to='planiranje.PlaniranoOpravilo'),
        ),
        migrations.AddField(
            model_name='plan',
            name='sklop',
            field=models.ForeignKey(to='planiranje.SkupinaPlanov'),
        ),
        migrations.AddField(
            model_name='plan',
            name='zahtevek',
            field=models.ForeignKey(null=True, blank=True, to='zahtevki.Zahtevek'),
        ),
    ]
