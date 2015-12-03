# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predpisi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtikelPlan',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('naziv', models.CharField(max_length=255)),
                ('perioda_predpisana_enota', models.CharField(verbose_name='enota periode', choices=[('dan', 'Dan'), ('teden', 'Teden'), ('mesec', 'Mesec'), ('leto', 'Leto')], max_length=5)),
                ('perioda_predpisana_enota_kolicina', models.IntegerField(verbose_name='kolicina enote periode')),
                ('perioda_predpisana_kolicina_na_enoto', models.IntegerField(verbose_name='kolicina na enoto periode')),
            ],
            options={
                'verbose_name': 'Plan Obratovanja in Vzdrževanja',
                'verbose_name_plural': 'Plan Obratovanja in Vzdrževanja',
            },
        ),
        migrations.CreateModel(
            name='ModelArtikla',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('naziv', models.CharField(max_length=255)),
                ('P1_title', models.CharField(verbose_name='P1 title', null=True, max_length=255, blank=True)),
                ('P1_value', models.CharField(verbose_name='P1 value', null=True, max_length=255, blank=True)),
                ('P2_title', models.CharField(verbose_name='P2 title', null=True, max_length=255, blank=True)),
                ('P2_value', models.CharField(verbose_name='P2 value', null=True, max_length=255, blank=True)),
                ('P3_title', models.CharField(verbose_name='P3 title', null=True, max_length=255, blank=True)),
                ('P3_value', models.CharField(verbose_name='P3 value', null=True, max_length=255, blank=True)),
                ('P4_title', models.CharField(verbose_name='P4 title', null=True, max_length=255, blank=True)),
                ('P4_value', models.CharField(verbose_name='P4 value', null=True, max_length=255, blank=True)),
                ('P5_title', models.CharField(verbose_name='P5 title', null=True, max_length=255, blank=True)),
                ('P5_value', models.CharField(verbose_name='P5 value', null=True, max_length=255, blank=True)),
            ],
            options={
                'verbose_name': 'model artikla',
                'ordering': ('naziv',),
                'verbose_name_plural': 'modeli artiklov',
            },
        ),
        migrations.CreateModel(
            name='ObratovalniParameter',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('enota', models.CharField(max_length=20, blank=True)),
                ('opis', models.CharField(verbose_name='opis', max_length=255, blank=True)),
                ('artikel', models.ForeignKey(to='katalog.ModelArtikla', null=True, blank=True)),
            ],
            options={
                'verbose_name': 'obratovalni parameter',
                'verbose_name_plural': 'obratovalni parametri',
            },
        ),
        migrations.CreateModel(
            name='Proizvajalec',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
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
        migrations.AddField(
            model_name='artikelplan',
            name='artikel',
            field=models.ForeignKey(to='katalog.ModelArtikla'),
        ),
        migrations.AddField(
            model_name='artikelplan',
            name='predpis_opravilo',
            field=models.ForeignKey(to='predpisi.PredpisOpravilo', null=True, blank=True),
        ),
    ]
