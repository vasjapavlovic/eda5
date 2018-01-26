# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delovninalogi', '0001_initial'),
        ('deli', '0001_initial'),
        ('core', '0001_initial'),
        ('partnerji', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Konto',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=10, unique=True)),
                ('naziv', models.CharField(max_length=50)),
                ('zap_st', models.IntegerField(verbose_name='zaporedna Številka', default=0)),
            ],
            options={
                'verbose_name_plural': 'konti',
                'verbose_name': 'konto',
                'ordering': ('zap_st',),
            },
        ),
        migrations.CreateModel(
            name='PodKonto',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=10, unique=True)),
                ('naziv', models.CharField(max_length=50)),
                ('zap_st', models.IntegerField(verbose_name='zaporedna Številka', default=0)),
                ('skupina', models.ForeignKey(to='racunovodstvo.Konto')),
            ],
            options={
                'verbose_name_plural': 'pod konti',
                'verbose_name': 'pod konto',
                'ordering': ('zap_st',),
            },
        ),
        migrations.CreateModel(
            name='Racun',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_likvidiran', models.BooleanField(default=False)),
                ('oznaka', models.IntegerField()),
                ('davcna_klasifikacija', models.IntegerField(choices=[(0, 'podjetje'), (1, 'razdelilnik')])),
                ('valuta', models.DateField(blank=True, null=True)),
                ('datum_storitve_od', models.DateField(blank=True, null=True)),
                ('datum_storitve_do', models.DateField(blank=True, null=True)),
                ('je_reprezentanca', models.BooleanField(default=False)),
                ('reprezentanca_opis', models.CharField(blank=True, max_length=255, null=True)),
                ('zavrnjen', models.BooleanField(default=False)),
                ('zavrnjen_datum', models.DateField(blank=True, null=True)),
                ('zavrnjen_obrazlozitev_text', models.TextField(blank=True, null=True)),
                ('povracilo_stroskov_zaposlenemu', models.ForeignKey(null=True, blank=True, to='partnerji.Oseba')),
                ('racunovodsko_leto', models.ForeignKey(to='core.ObdobjeLeto')),
                ('stavba', models.ForeignKey(null=True, blank=True, to='deli.Stavba')),
            ],
            options={
                'verbose_name_plural': 'računi',
                'verbose_name': 'račun',
                'ordering': ('-racunovodsko_leto', '-oznaka'),
            },
        ),
        migrations.CreateModel(
            name='SkupinaVrsteStroska',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=20, unique=True)),
                ('naziv', models.CharField(max_length=200)),
                ('zap_st', models.IntegerField(verbose_name='zaporedna Številka', default=0)),
                ('skupina', models.ForeignKey(to='racunovodstvo.PodKonto')),
            ],
            options={
                'verbose_name_plural': 'skupine vrst stroškov',
                'verbose_name': 'skupina vrste stroška',
                'ordering': ('zap_st',),
            },
        ),
        migrations.CreateModel(
            name='Strosek',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=200)),
                ('datum_storitve_od', models.DateField()),
                ('datum_storitve_do', models.DateField()),
                ('osnova', models.DecimalField(verbose_name='osnova za ddv', max_digits=10, decimal_places=5)),
                ('stopnja_ddv', models.IntegerField(verbose_name='stopnja DDV', choices=[(0, 'neobdavčeno'), (1, 'nižja stopnja'), (2, 'višja stopnja')])),
                ('delovni_nalog', models.OneToOneField(null=True, blank=True, to='delovninalogi.DelovniNalog')),
                ('racun', models.ForeignKey(to='racunovodstvo.Racun')),
            ],
            options={
                'verbose_name_plural': 'stroški',
                'verbose_name': 'strošek',
                'ordering': ('-racun__racunovodsko_leto', '-racun__oznaka', 'oznaka'),
            },
        ),
        migrations.CreateModel(
            name='VrstaStroska',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=20, unique=True)),
                ('naziv', models.CharField(max_length=200)),
                ('zap_st', models.IntegerField(verbose_name='zaporedna Številka', default=0)),
                ('skupina', models.ForeignKey(to='racunovodstvo.SkupinaVrsteStroska')),
            ],
            options={
                'verbose_name_plural': 'vrste stroškov',
                'verbose_name': 'vrsta stroška',
                'ordering': ('zap_st',),
            },
        ),
        migrations.AddField(
            model_name='strosek',
            name='vrsta_stroska',
            field=models.ForeignKey(to='racunovodstvo.VrstaStroska'),
        ),
    ]
