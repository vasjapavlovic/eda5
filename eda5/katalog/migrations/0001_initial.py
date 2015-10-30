# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0008_auto_20151026_0727'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelArtikla',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('P1_title', models.CharField(max_length=255, null=True, verbose_name='P1 title', blank=True)),
                ('P1_value', models.CharField(max_length=255, null=True, verbose_name='P1 value', blank=True)),
                ('P2_title', models.CharField(max_length=255, null=True, verbose_name='P2 title', blank=True)),
                ('P2_value', models.CharField(max_length=255, null=True, verbose_name='P2 value', blank=True)),
                ('P3_title', models.CharField(max_length=255, null=True, verbose_name='P3 title', blank=True)),
                ('P3_value', models.CharField(max_length=255, null=True, verbose_name='P3 value', blank=True)),
                ('P4_title', models.CharField(max_length=255, null=True, verbose_name='P4 title', blank=True)),
                ('P4_value', models.CharField(max_length=255, null=True, verbose_name='P4 value', blank=True)),
                ('P5_title', models.CharField(max_length=255, null=True, verbose_name='P5 title', blank=True)),
                ('P5_value', models.CharField(max_length=255, null=True, verbose_name='P5 value', blank=True)),
                ('dokumentacija', models.ManyToManyField(to='posta.Dokument')),
            ],
            options={
                'verbose_name_plural': 'modeli artiklov',
                'ordering': ('naziv',),
                'verbose_name': 'model artikla',
            },
        ),
        migrations.CreateModel(
            name='PlanOV',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('oznaka', models.CharField(max_length=25)),
                ('naziv', models.CharField(max_length=255)),
                ('perioda_predpisana_enota', models.CharField(max_length=5, verbose_name='enota periode', choices=[('Dan', 'Dan'), ('Teden', 'Teden'), ('Mesec', 'Mesec'), ('Leto', 'Leto')])),
                ('perioda_predpisana_enota_kolicina', models.IntegerField(verbose_name='kolicina enote periode')),
                ('perioda_predpisana_kolicina_na_enoto', models.IntegerField(verbose_name='kolicina na enoto periode')),
                ('element', models.ForeignKey(to='katalog.ModelArtikla')),
            ],
            options={
                'verbose_name_plural': 'Plan Obratovanja in Vzdrževanja',
                'verbose_name': 'Plan Obratovanja in Vzdrževanja',
            },
        ),
        migrations.CreateModel(
            name='Proizvajalec',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('naziv', models.CharField(unique=True, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'proizvajalci',
                'ordering': ('naziv',),
                'verbose_name': 'proizvajalec',
            },
        ),
        migrations.CreateModel(
            name='RezervniDel',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('naziv', models.CharField(max_length=255)),
                ('oznaka', models.CharField(max_length=25, blank=True)),
                ('artikel', models.ForeignKey(to='katalog.ModelArtikla')),
            ],
            options={
                'verbose_name_plural': 'Rezervni Deli',
                'verbose_name': 'Rezervni Del',
            },
        ),
        migrations.CreateModel(
            name='TipArtikla',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'tipi artiklov',
                'ordering': ('oznaka',),
                'verbose_name': 'tip artikla',
            },
        ),
        migrations.AddField(
            model_name='modelartikla',
            name='proizvajalec',
            field=models.ForeignKey(to='katalog.Proizvajalec'),
        ),
        migrations.AddField(
            model_name='modelartikla',
            name='tip',
            field=models.ForeignKey(to='katalog.TipArtikla'),
        ),
    ]
