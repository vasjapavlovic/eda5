# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '__first__'),
        ('deli', '0001_initial'),
        ('core', '__first__'),
        ('delovninalogi', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Konto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('oznaka', models.CharField(unique=True, max_length=10)),
                ('naziv', models.CharField(max_length=50)),
                ('zap_st', models.IntegerField(default=0, verbose_name='zaporedna Številka')),
            ],
            options={
                'verbose_name': 'konto',
                'ordering': ('zap_st',),
                'verbose_name_plural': 'konti',
            },
        ),
        migrations.CreateModel(
            name='PodKonto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('oznaka', models.CharField(unique=True, max_length=10)),
                ('naziv', models.CharField(max_length=50)),
                ('zap_st', models.IntegerField(default=0, verbose_name='zaporedna Številka')),
                ('skupina', models.ForeignKey(to='racunovodstvo.Konto')),
            ],
            options={
                'verbose_name': 'pod konto',
                'ordering': ('zap_st',),
                'verbose_name_plural': 'pod konti',
            },
        ),
        migrations.CreateModel(
            name='Racun',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_likvidiran', models.BooleanField(default=False)),
                ('oznaka', models.IntegerField()),
                ('davcna_klasifikacija', models.IntegerField(choices=[(0, 'podjetje'), (1, 'razdelilnik')])),
                ('valuta', models.DateField(null=True, blank=True)),
                ('datum_storitve_od', models.DateField(null=True, blank=True)),
                ('datum_storitve_do', models.DateField(null=True, blank=True)),
                ('je_reprezentanca', models.BooleanField(default=False)),
                ('reprezentanca_opis', models.CharField(null=True, blank=True, max_length=255)),
                ('zavrnjen', models.BooleanField(default=False)),
                ('zavrnjen_datum', models.DateField(null=True, blank=True)),
                ('zavrnjen_obrazlozitev_text', models.TextField(null=True, blank=True)),
                ('povracilo_stroskov_zaposlenemu', models.ForeignKey(null=True, blank=True, to='partnerji.Oseba')),
                ('racunovodsko_leto', models.ForeignKey(to='core.ObdobjeLeto')),
                ('stavba', models.ForeignKey(null=True, blank=True, to='deli.Stavba')),
            ],
            options={
                'verbose_name': 'račun',
                'ordering': ('-racunovodsko_leto', '-oznaka'),
                'verbose_name_plural': 'računi',
            },
        ),
        migrations.CreateModel(
            name='SkupinaVrsteStroska',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('oznaka', models.CharField(unique=True, max_length=20)),
                ('naziv', models.CharField(max_length=200)),
                ('zap_st', models.IntegerField(default=0, verbose_name='zaporedna Številka')),
                ('skupina', models.ForeignKey(to='racunovodstvo.PodKonto')),
            ],
            options={
                'verbose_name': 'skupina vrste stroška',
                'ordering': ('zap_st',),
                'verbose_name_plural': 'skupine vrst stroškov',
            },
        ),
        migrations.CreateModel(
            name='Strosek',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=200)),
                ('datum_storitve_od', models.DateField()),
                ('datum_storitve_do', models.DateField()),
                ('osnova', models.DecimalField(max_digits=10, verbose_name='osnova za ddv', decimal_places=5)),
                ('stopnja_ddv', models.IntegerField(choices=[(0, 'neobdavčeno'), (1, 'nižja stopnja'), (2, 'višja stopnja')], verbose_name='stopnja DDV')),
                ('delovni_nalog', models.OneToOneField(null=True, to='delovninalogi.DelovniNalog', blank=True)),
                ('racun', models.ForeignKey(to='racunovodstvo.Racun')),
            ],
            options={
                'verbose_name': 'strošek',
                'ordering': ('-racun__racunovodsko_leto', '-racun__oznaka', 'oznaka'),
                'verbose_name_plural': 'stroški',
            },
        ),
        migrations.CreateModel(
            name='VrstaStroska',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('oznaka', models.CharField(unique=True, max_length=20)),
                ('naziv', models.CharField(max_length=200)),
                ('zap_st', models.IntegerField(default=0, verbose_name='zaporedna Številka')),
                ('skupina', models.ForeignKey(to='racunovodstvo.SkupinaVrsteStroska')),
            ],
            options={
                'verbose_name': 'vrsta stroška',
                'ordering': ('zap_st',),
                'verbose_name_plural': 'vrste stroškov',
            },
        ),
        migrations.AddField(
            model_name='strosek',
            name='vrsta_stroska',
            field=models.ForeignKey(to='racunovodstvo.VrstaStroska'),
        ),
    ]
