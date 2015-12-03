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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('priimek', models.CharField(max_length=50)),
                ('ime', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('A', 'pooblaščenec'), ('B', 'delavec')], max_length=1)),
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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('postna_stevilka', models.CharField(verbose_name='poštna številka', max_length=10, unique=True)),
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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('iban', models.CharField(verbose_name='stevilka računa', max_length=20, unique=True)),
                ('banka', models.ForeignKey(to='partnerji.Banka')),
                ('partner', models.ForeignKey(to='partnerji.Partner', verbose_name='partner')),
            ],
            options={
                'verbose_name': 'TR Račun',
                'verbose_name_plural': 'TR Računi',
            },
        ),
        migrations.AddField(
            model_name='partner',
            name='posta',
            field=models.ForeignKey(to='partnerji.Posta', verbose_name='pošta'),
        ),
    ]
