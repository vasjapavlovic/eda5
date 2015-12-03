# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0001_initial'),
        ('katalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('naziv_opravila_izven_plana', models.CharField(max_length=255, blank=True)),
                ('artikel_plan', models.ForeignKey(to='katalog.ArtikelPlan', null=True, blank=True)),
                ('element', models.ForeignKey(to='deli.Element', null=True, blank=True)),
            ],
            options={
                'verbose_name': 'planirana aktivnost',
                'verbose_name_plural': 'planirane aktivnosti',
            },
        ),
        migrations.CreateModel(
            name='PlaniranoOpravilo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('oznaka', models.CharField(max_length=25)),
                ('naziv', models.CharField(max_length=255)),
                ('namen', models.CharField(max_length=255)),
                ('obseg', models.TextField()),
                ('perioda_predpisana_enota', models.CharField(verbose_name='enota periode', choices=[('dan', 'Dan'), ('teden', 'Teden'), ('mesec', 'Mesec'), ('leto', 'Leto')], max_length=5)),
                ('perioda_predpisana_enota_kolicina', models.IntegerField(verbose_name='kolicina enote periode')),
                ('perioda_predpisana_kolicina_na_enoto', models.IntegerField(verbose_name='kolicina na enoto periode')),
                ('opomba', models.TextField(blank=True)),
                ('plan', models.ForeignKey(to='planiranje.Plan')),
            ],
            options={
                'verbose_name': 'planirano opravilo',
                'verbose_name_plural': 'planirana opravila',
            },
        ),
        migrations.CreateModel(
            name='SkupinaPlanov',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
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
            field=models.ForeignKey(to='planiranje.PlaniranoOpravilo', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='plan',
            name='sklop',
            field=models.ForeignKey(to='planiranje.SkupinaPlanov'),
        ),
    ]
