# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelArtikla',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('P1_title', models.CharField(max_length=255, blank=True, null=True, verbose_name='P1 title')),
                ('P1_value', models.CharField(max_length=255, blank=True, null=True, verbose_name='P1 value')),
                ('P2_title', models.CharField(max_length=255, blank=True, null=True, verbose_name='P2 title')),
                ('P2_value', models.CharField(max_length=255, blank=True, null=True, verbose_name='P2 value')),
                ('P3_title', models.CharField(max_length=255, blank=True, null=True, verbose_name='P3 title')),
                ('P3_value', models.CharField(max_length=255, blank=True, null=True, verbose_name='P3 value')),
                ('P4_title', models.CharField(max_length=255, blank=True, null=True, verbose_name='P4 title')),
                ('P4_value', models.CharField(max_length=255, blank=True, null=True, verbose_name='P4 value')),
                ('P5_title', models.CharField(max_length=255, blank=True, null=True, verbose_name='P5 title')),
                ('P5_value', models.CharField(max_length=255, blank=True, null=True, verbose_name='P5 value')),
            ],
            options={
                'verbose_name': 'model artikla',
                'verbose_name_plural': 'modeli artiklov',
                'ordering': ('naziv',),
            },
        ),
        migrations.CreateModel(
            name='PlanOV',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('naziv', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'proizvajalec',
                'verbose_name_plural': 'proizvajalci',
                'ordering': ('naziv',),
            },
        ),
        migrations.CreateModel(
            name='RezervniDel',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'tip artikla',
                'verbose_name_plural': 'tipi artiklov',
                'ordering': ('oznaka',),
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
