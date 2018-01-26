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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('naziv', models.CharField(max_length=255)),
                ('perioda_predpisana_enota', models.CharField(verbose_name='enota periode', max_length=5, choices=[('dan', 'Dan'), ('teden', 'Teden'), ('mesec', 'Mesec'), ('leto', 'Leto')])),
                ('perioda_predpisana_enota_kolicina', models.IntegerField(verbose_name='kolicina enote periode')),
                ('perioda_predpisana_kolicina_na_enoto', models.IntegerField(verbose_name='kolicina na enoto periode')),
            ],
            options={
                'verbose_name_plural': 'Plan Obratovanja in Vzdrževanja',
                'verbose_name': 'Plan Obratovanja in Vzdrževanja',
            },
        ),
        migrations.CreateModel(
            name='Karakteristika',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=20)),
                ('enota', models.CharField(blank=True, max_length=20)),
                ('opis', models.CharField(blank=True, max_length=255, verbose_name='opis')),
            ],
            options={
                'verbose_name_plural': 'karakteristike artiklov',
                'verbose_name': 'karakteristika artikla',
            },
        ),
        migrations.CreateModel(
            name='KarakteristikaVrednost',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('vrednost', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'vrednosti karakteristik',
                'verbose_name': 'vrednost karakteristike',
            },
        ),
        migrations.CreateModel(
            name='ModelArtikla',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=20, unique=True)),
                ('naziv', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'modeli artiklov',
                'verbose_name': 'model artikla',
                'ordering': ('naziv',),
            },
        ),
        migrations.CreateModel(
            name='ObratovalniParameter',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=20)),
                ('enota', models.CharField(blank=True, max_length=20)),
                ('opis', models.CharField(blank=True, max_length=255, verbose_name='opis')),
            ],
            options={
                'verbose_name_plural': 'obratovalni parametri',
                'verbose_name': 'obratovalni parameter',
            },
        ),
        migrations.CreateModel(
            name='Proizvajalec',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=20, unique=True)),
                ('naziv', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'proizvajalci',
                'verbose_name': 'proizvajalec',
                'ordering': ('naziv',),
            },
        ),
        migrations.CreateModel(
            name='RezervniDel',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('naziv', models.CharField(max_length=255)),
                ('oznaka', models.CharField(blank=True, max_length=25)),
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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=20, unique=True)),
                ('naziv', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'tipi artiklov',
                'verbose_name': 'tip artikla',
                'ordering': ('oznaka',),
            },
        ),
        migrations.AddField(
            model_name='obratovalniparameter',
            name='tip_artikla',
            field=models.ForeignKey(null=True, blank=True, to='katalog.TipArtikla'),
        ),
        migrations.AddField(
            model_name='modelartikla',
            name='proizvajalec',
            field=models.ForeignKey(to='katalog.Proizvajalec'),
        ),
        migrations.AddField(
            model_name='modelartikla',
            name='tip_artikla',
            field=models.ForeignKey(to='katalog.TipArtikla'),
        ),
        migrations.AddField(
            model_name='karakteristikavrednost',
            name='artikel',
            field=models.ForeignKey(null=True, blank=True, to='katalog.ModelArtikla'),
        ),
        migrations.AddField(
            model_name='karakteristikavrednost',
            name='karakteristika',
            field=models.ForeignKey(to='katalog.Karakteristika'),
        ),
        migrations.AddField(
            model_name='karakteristika',
            name='tip_artikla',
            field=models.ForeignKey(null=True, blank=True, to='katalog.TipArtikla'),
        ),
        migrations.AddField(
            model_name='artikelplan',
            name='artikel',
            field=models.ForeignKey(to='katalog.ModelArtikla'),
        ),
        migrations.AddField(
            model_name='artikelplan',
            name='predpis_opravilo',
            field=models.ForeignKey(null=True, blank=True, to='predpisi.PredpisOpravilo'),
        ),
    ]
