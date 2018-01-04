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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('iso_koda', models.CharField(max_length=3, unique=True)),
                ('naziv', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Država',
                'verbose_name_plural': 'Države',
            },
        ),
        migrations.CreateModel(
            name='Oseba',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('priimek', models.CharField(max_length=50)),
                ('ime', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=1, choices=[('A', 'pooblaščenec'), ('B', 'delavec')])),
                ('kvalifikacije', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Oseba',
                'ordering': ['priimek'],
                'verbose_name_plural': 'Osebe',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('kratko_ime', models.CharField(verbose_name='Kratko Ime', max_length=100)),
                ('naslov', models.CharField(verbose_name='Naslov', max_length=255)),
                ('is_pravnaoseba', models.NullBooleanField()),
                ('davcni_zavezanec', models.NullBooleanField()),
                ('davcna_st', models.CharField(max_length=15, blank=True, unique=True)),
                ('maticna_st', models.CharField(max_length=15, blank=True)),
                ('dolgo_ime', models.CharField(max_length=255, blank=True)),
                ('kontakt_tel', models.CharField(max_length=30, null=True, blank=True)),
                ('kontakt_email', models.CharField(max_length=30, null=True, blank=True)),
                ('is_skupina_partnerjev', models.NullBooleanField(verbose_name='Skupina partnerjev?', default=False)),
                ('opis_skupine_partnerjev', models.CharField(verbose_name='opis skupine partnerjev', max_length=255, null=True, blank=True)),
                ('partner_skupina', models.ManyToManyField(to='partnerji.Partner', blank=True, related_name='_partner_skupina_+')),
            ],
            options={
                'verbose_name': 'partner',
                'ordering': ['kratko_ime'],
                'verbose_name_plural': 'partnerji',
            },
        ),
        migrations.CreateModel(
            name='Posta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('postna_stevilka', models.CharField(verbose_name='poštna številka', max_length=10, unique=True)),
                ('naziv', models.CharField(max_length=100)),
                ('drzava', models.ForeignKey(to='partnerji.Drzava')),
            ],
            options={
                'verbose_name': 'Pošta',
                'ordering': ['postna_stevilka'],
                'verbose_name_plural': 'Pošte',
            },
        ),
        migrations.CreateModel(
            name='SkupinaPartnerjev',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('naziv', models.CharField(max_length=255)),
                ('oznaka', models.CharField(max_length=20, blank=True)),
                ('partner', models.ManyToManyField(to='partnerji.Partner')),
            ],
            options={
                'verbose_name': 'skupina partnerjev',
                'ordering': ['naziv'],
                'verbose_name_plural': 'skupine partnerjev',
            },
        ),
        migrations.CreateModel(
            name='TRRacun',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('iban', models.CharField(verbose_name='stevilka računa', max_length=20, unique=True)),
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
        migrations.AddField(
            model_name='oseba',
            name='podjetje',
            field=models.ForeignKey(to='partnerji.Partner'),
        ),
    ]
