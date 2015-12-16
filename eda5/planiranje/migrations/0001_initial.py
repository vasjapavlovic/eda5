# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0001_initial'),
        ('deli', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('oznaka', models.CharField(max_length=25)),
                ('naziv', models.CharField(max_length=255)),
                ('zap_st', models.IntegerField(default=0, verbose_name='zaporedna številka')),
                ('opis', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'plani',
                'verbose_name': 'plan',
            },
        ),
        migrations.CreateModel(
            name='PlaniranaAktivnost',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('naziv_opravila_izven_plana', models.CharField(blank=True, max_length=255)),
                ('artikel_plan', models.ForeignKey(to='katalog.ArtikelPlan', blank=True, null=True)),
                ('element', models.ForeignKey(to='deli.Element', blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'planirane aktivnosti',
                'verbose_name': 'planirana aktivnost',
            },
        ),
        migrations.CreateModel(
            name='PlaniranoOpravilo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('oznaka', models.CharField(max_length=25)),
                ('naziv', models.CharField(max_length=255)),
                ('namen', models.CharField(max_length=255)),
                ('obseg', models.TextField()),
                ('perioda_predpisana_enota', models.CharField(choices=[('dan', 'Dan'), ('teden', 'Teden'), ('mesec', 'Mesec'), ('leto', 'Leto')], max_length=5, verbose_name='enota periode')),
                ('perioda_predpisana_enota_kolicina', models.IntegerField(verbose_name='kolicina enote periode')),
                ('perioda_predpisana_kolicina_na_enoto', models.IntegerField(verbose_name='kolicina na enoto periode')),
                ('opomba', models.TextField(blank=True)),
                ('plan', models.ForeignKey(to='planiranje.Plan')),
            ],
            options={
                'verbose_name_plural': 'planirana opravila',
                'verbose_name': 'planirano opravilo',
            },
        ),
        migrations.CreateModel(
            name='SkupinaPlanov',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('oznaka', models.CharField(max_length=25)),
                ('naziv', models.CharField(max_length=255)),
                ('zap_st', models.IntegerField(default=0, verbose_name='zaporedna številka')),
            ],
            options={
                'verbose_name_plural': 'skupine planov',
                'verbose_name': 'skupina planov',
                'ordering': ('zap_st',),
            },
        ),
        migrations.AddField(
            model_name='planiranaaktivnost',
            name='planirano_opravilo',
            field=models.ForeignKey(to='planiranje.PlaniranoOpravilo', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plan',
            name='sklop',
            field=models.ForeignKey(to='planiranje.SkupinaPlanov'),
        ),
    ]
