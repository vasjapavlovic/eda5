# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0008_auto_20151026_0727'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
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
            name='PlanIzdaja',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('datum_izdaje', models.DateTimeField()),
                ('plan', models.ForeignKey(to='planiranje.Plan')),
                ('potrditvena_dokumentacija', models.ForeignKey(to='posta.Dokument')),
            ],
            options={
                'verbose_name': 'izdaja plana',
                'verbose_name_plural': 'izdaje planov',
            },
        ),
        migrations.CreateModel(
            name='PlanOpravilo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('oznaka', models.CharField(max_length=25)),
                ('naziv', models.CharField(max_length=255)),
                ('namen', models.CharField(max_length=255)),
                ('obseg', models.TextField()),
                ('perioda_predpisana_enota', models.CharField(verbose_name='enota periode', max_length=5, choices=[('dan', 'Dan'), ('teden', 'Teden'), ('mesec', 'Mesec'), ('leto', 'Leto')])),
                ('perioda_predpisana_enota_kolicina', models.IntegerField(verbose_name='kolicina enote periode')),
                ('perioda_predpisana_kolicina_na_enoto', models.IntegerField(verbose_name='kolicina na enoto periode')),
                ('zap_st', models.IntegerField(verbose_name='zaporedna številka', default=0)),
                ('opomba', models.TextField()),
                ('plan', models.ForeignKey(to='planiranje.PlanIzdaja', verbose_name='izdaja plana')),
            ],
            options={
                'verbose_name': 'planirano opravilo',
                'verbose_name_plural': 'planirana opravila',
            },
        ),
        migrations.CreateModel(
            name='SklopPlanov',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('oznaka', models.CharField(max_length=25)),
                ('naziv', models.CharField(max_length=255)),
                ('zap_st', models.IntegerField(verbose_name='zaporedna številka', default=0)),
            ],
            options={
                'ordering': ('zap_st',),
                'verbose_name': 'sklop planov',
                'verbose_name_plural': 'sklopi planov',
            },
        ),
        migrations.AddField(
            model_name='plan',
            name='sklop',
            field=models.ForeignKey(to='planiranje.SklopPlanov'),
        ),
    ]
