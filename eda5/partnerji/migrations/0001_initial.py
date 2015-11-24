# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banka',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('bic_koda', models.CharField(max_length=8, unique=True)),
                ('bancna_oznaka', models.CharField(max_length=2, unique=True)),
            ],
            options={
                'verbose_name': 'Banka',
                'verbose_name_plural': 'Banke',
            },
        ),
        migrations.CreateModel(
            name='Drzava',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=100)),
                ('iso_koda', models.CharField(max_length=3, unique=True)),
            ],
            options={
                'verbose_name': 'Država',
                'verbose_name_plural': 'Države',
            },
        ),
        migrations.CreateModel(
            name='Oseba',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('priimek', models.CharField(max_length=50)),
                ('ime', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=1, choices=[('A', 'pooblaščenec'), ('B', 'delavec')])),
                ('kvalifikacije', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Oseba',
                'verbose_name_plural': 'Osebe',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('kratko_ime', models.CharField(max_length=100)),
                ('naslov', models.CharField(max_length=255)),
                ('is_pravnaoseba', models.BooleanField()),
                ('davcni_zavezanec', models.BooleanField()),
                ('davcna_st', models.CharField(max_length=15, unique=True, blank=True)),
                ('maticna_st', models.CharField(max_length=15, unique=True, blank=True)),
                ('dolgo_ime', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'verbose_name': 'partner',
                'verbose_name_plural': 'partnerji',
            },
        ),
        migrations.CreateModel(
            name='Posta',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('postna_stevilka', models.CharField(max_length=10, unique=True, verbose_name='poštna številka')),
                ('naziv', models.CharField(max_length=100)),
                ('drzava', models.ForeignKey(to='partnerji.Drzava')),
            ],
            options={
                'verbose_name': 'Pošta',
                'verbose_name_plural': 'Pošte',
            },
        ),
        migrations.CreateModel(
            name='SkupinaPartnerjev',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('naziv', models.CharField(max_length=255)),
                ('oznaka', models.CharField(max_length=20, blank=True)),
                ('partner', models.ManyToManyField(to='partnerji.Partner')),
            ],
            options={
                'verbose_name': 'skupina partnerjev',
                'verbose_name_plural': 'skupine partnerjev',
            },
        ),
        migrations.CreateModel(
            name='TRRacun',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('iban', models.CharField(max_length=20, unique=True, verbose_name='stevilka računa')),
                ('banka', models.ForeignKey(to='partnerji.Banka')),
                ('partner', models.ForeignKey(verbose_name='partner', to='partnerji.Partner')),
            ],
            options={
                'verbose_name': 'TR Račun',
                'verbose_name_plural': 'TR Računi',
            },
        ),
        migrations.AddField(
            model_name='partner',
            name='posta',
            field=models.ForeignKey(verbose_name='pošta', to='partnerji.Posta'),
        ),
    ]
