# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Banka',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('iso_koda', models.CharField(max_length=3, unique=True)),
                ('naziv', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Države',
                'verbose_name': 'Država',
            },
        ),
        migrations.CreateModel(
            name='Oseba',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('priimek', models.CharField(max_length=50)),
                ('ime', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=1, choices=[('A', 'pooblaščenec'), ('B', 'delavec')])),
                ('kvalifikacije', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Osebe',
                'verbose_name': 'Oseba',
                'ordering': ['priimek'],
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('kratko_ime', models.CharField(verbose_name='Kratko Ime', max_length=100)),
                ('naslov', models.CharField(verbose_name='Naslov', max_length=255)),
                ('is_pravnaoseba', models.NullBooleanField()),
                ('davcni_zavezanec', models.NullBooleanField()),
                ('davcna_st', models.CharField(blank=True, max_length=15, unique=True)),
                ('maticna_st', models.CharField(blank=True, max_length=15)),
                ('dolgo_ime', models.CharField(blank=True, max_length=255)),
                ('kontakt_tel', models.CharField(blank=True, max_length=30, null=True)),
                ('kontakt_email', models.CharField(blank=True, max_length=30, null=True)),
                ('is_skupina_partnerjev', models.NullBooleanField(default=False, verbose_name='Skupina partnerjev?')),
                ('opis_skupine_partnerjev', models.CharField(blank=True, max_length=255, null=True, verbose_name='opis skupine partnerjev')),
                ('partner_skupina', models.ManyToManyField(blank=True, related_name='_partner_skupina_+', to='partnerji.Partner')),
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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('postna_stevilka', models.CharField(verbose_name='poštna številka', max_length=10, unique=True)),
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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('iban', models.CharField(verbose_name='stevilka računa', max_length=20, unique=True)),
                ('banka', models.ForeignKey(to='partnerji.Banka')),
                ('partner', models.ForeignKey(verbose_name='partner', to='partnerji.Partner')),
            ],
            options={
                'verbose_name_plural': 'TR Računi',
                'verbose_name': 'TR Račun',
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
        migrations.AddField(
            model_name='oseba',
            name='user',
            field=models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='banka',
            name='partner',
            field=models.OneToOneField(blank=True, to='partnerji.Partner'),
        ),
    ]
