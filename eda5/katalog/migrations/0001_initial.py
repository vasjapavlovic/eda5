# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelArtikla',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('P1_title', models.CharField(max_length=255, verbose_name='P1 title', blank=True, null=True)),
                ('P1_value', models.CharField(max_length=255, verbose_name='P1 value', blank=True, null=True)),
                ('P2_title', models.CharField(max_length=255, verbose_name='P2 title', blank=True, null=True)),
                ('P2_value', models.CharField(max_length=255, verbose_name='P2 value', blank=True, null=True)),
                ('P3_title', models.CharField(max_length=255, verbose_name='P3 title', blank=True, null=True)),
                ('P3_value', models.CharField(max_length=255, verbose_name='P3 value', blank=True, null=True)),
                ('P4_title', models.CharField(max_length=255, verbose_name='P4 title', blank=True, null=True)),
                ('P4_value', models.CharField(max_length=255, verbose_name='P4 value', blank=True, null=True)),
                ('P5_title', models.CharField(max_length=255, verbose_name='P5 title', blank=True, null=True)),
                ('P5_value', models.CharField(max_length=255, verbose_name='P5 value', blank=True, null=True)),
                ('prejeta_dokumentacija', models.ManyToManyField(to='posta.Dokument', blank=True)),
            ],
            options={
                'verbose_name': 'model artikla',
                'ordering': ('naziv',),
                'verbose_name_plural': 'modeli artiklov',
            },
        ),
        migrations.CreateModel(
            name='PlanOV',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('oznaka', models.CharField(max_length=25)),
                ('naziv', models.CharField(max_length=255)),
                ('perioda_predpisana_enota', models.CharField(max_length=5, choices=[('dan', 'Dan'), ('teden', 'Teden'), ('mesec', 'Mesec'), ('leto', 'Leto')], verbose_name='enota periode')),
                ('perioda_predpisana_enota_kolicina', models.IntegerField(verbose_name='kolicina enote periode')),
                ('perioda_predpisana_kolicina_na_enoto', models.IntegerField(verbose_name='kolicina na enoto periode')),
                ('element', models.ForeignKey(to='katalog.ModelArtikla')),
            ],
            options={
                'verbose_name': 'Plan Obratovanja in Vzdrževanja',
                'verbose_name_plural': 'Plan Obratovanja in Vzdrževanja',
            },
        ),
        migrations.CreateModel(
            name='Proizvajalec',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('naziv', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'proizvajalec',
                'ordering': ('naziv',),
                'verbose_name_plural': 'proizvajalci',
            },
        ),
        migrations.CreateModel(
            name='RezervniDel',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('naziv', models.CharField(max_length=255)),
                ('oznaka', models.CharField(max_length=25, blank=True)),
                ('artikel', models.ForeignKey(to='katalog.ModelArtikla')),
            ],
            options={
                'verbose_name': 'Rezervni Del',
                'verbose_name_plural': 'Rezervni Deli',
            },
        ),
        migrations.CreateModel(
            name='TipArtikla',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'tip artikla',
                'ordering': ('oznaka',),
                'verbose_name_plural': 'tipi artiklov',
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
