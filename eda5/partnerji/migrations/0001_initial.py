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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('bic_koda', models.CharField(max_length=8, unique=True)),
                ('bancna_oznaka', models.CharField(max_length=2, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Banke',
                'verbose_name': 'Banka',
            },
        ),
        migrations.CreateModel(
            name='Drzava',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('naziv', models.CharField(max_length=100)),
                ('iso_koda', models.CharField(max_length=3, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Države',
                'verbose_name': 'Država',
            },
        ),
        migrations.CreateModel(
            name='Oseba',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('priimek', models.CharField(max_length=50)),
                ('ime', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('A', 'pooblaščenec'), ('B', 'delavec')], max_length=1)),
                ('kvalifikacije', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Osebe',
                'verbose_name': 'Oseba',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('kratko_ime', models.CharField(max_length=100)),
                ('naslov', models.CharField(max_length=255)),
                ('is_pravnaoseba', models.BooleanField()),
                ('davcni_zavezanec', models.BooleanField()),
                ('davcna_st', models.CharField(blank=True, max_length=15, unique=True)),
                ('maticna_st', models.CharField(blank=True, max_length=15)),
                ('dolgo_ime', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name_plural': 'partnerji',
                'verbose_name': 'partner',
                'ordering': ['kratko_ime'],
            },
        ),
        migrations.CreateModel(
            name='Posta',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('postna_stevilka', models.CharField(max_length=10, verbose_name='poštna številka', unique=True)),
                ('naziv', models.CharField(max_length=100)),
                ('drzava', models.ForeignKey(to='partnerji.Drzava')),
            ],
            options={
                'verbose_name_plural': 'Pošte',
                'verbose_name': 'Pošta',
                'ordering': ['postna_stevilka'],
            },
        ),
        migrations.CreateModel(
            name='SkupinaPartnerjev',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('naziv', models.CharField(max_length=255)),
                ('oznaka', models.CharField(blank=True, max_length=20)),
                ('partner', models.ManyToManyField(to='partnerji.Partner')),
            ],
            options={
                'verbose_name_plural': 'skupine partnerjev',
                'verbose_name': 'skupina partnerjev',
                'ordering': ['naziv'],
            },
        ),
        migrations.CreateModel(
            name='TRRacun',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('iban', models.CharField(max_length=20, verbose_name='stevilka računa', unique=True)),
                ('banka', models.ForeignKey(to='partnerji.Banka')),
                ('partner', models.ForeignKey(to='partnerji.Partner', verbose_name='partner')),
            ],
            options={
                'verbose_name_plural': 'TR Računi',
                'verbose_name': 'TR Račun',
            },
        ),
        migrations.AddField(
            model_name='partner',
            name='posta',
            field=models.ForeignKey(to='partnerji.Posta', verbose_name='pošta'),
        ),
    ]
