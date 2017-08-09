# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etaznalastnina', '__first__'),
        ('delovninalogi', '__first__'),
        ('deli', '__first__'),
        ('partnerji', '__first__'),
        ('core', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Konto',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('oznaka', models.CharField(unique=True, max_length=10)),
                ('naziv', models.CharField(max_length=50)),
                ('zap_st', models.IntegerField(default=0, verbose_name='zaporedna Številka')),
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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('oznaka', models.CharField(unique=True, max_length=10)),
                ('naziv', models.CharField(max_length=50)),
                ('zap_st', models.IntegerField(default=0, verbose_name='zaporedna Številka')),
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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_likvidiran', models.BooleanField(default=False)),
                ('oznaka', models.IntegerField()),
                ('davcna_klasifikacija', models.IntegerField(choices=[(0, 'podjetje'), (1, 'razdelilnik')])),
                ('valuta', models.DateField(null=True, blank=True)),
                ('datum_storitve_od', models.DateField(null=True, blank=True)),
                ('datum_storitve_do', models.DateField(null=True, blank=True)),
                ('je_reprezentanca', models.BooleanField(default=False)),
                ('reprezentanca_opis', models.CharField(null=True, max_length=255, blank=True)),
                ('zavrnjen', models.BooleanField(default=False)),
                ('zavrnjen_datum', models.DateField(null=True, blank=True)),
                ('zavrnjen_obrazlozitev_text', models.TextField(null=True, blank=True)),
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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('oznaka', models.CharField(unique=True, max_length=20)),
                ('naziv', models.CharField(max_length=200)),
                ('zap_st', models.IntegerField(default=0, verbose_name='zaporedna Številka')),
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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=200)),
                ('datum_storitve_od', models.DateField()),
                ('datum_storitve_do', models.DateField()),
                ('osnova', models.DecimalField(max_digits=10, decimal_places=5, verbose_name='osnova za ddv')),
                ('stopnja_ddv', models.IntegerField(choices=[(0, 'neobdavčeno'), (1, 'nižja stopnja'), (2, 'višja stopnja')], verbose_name='stopnja DDV')),
                ('delilnik_vrsta', models.CharField(choices=[('fiksni', 'fiksni strošek'), ('vuporabi', 'LE v uporabi'), ('delilniki', 'po priloženem delilniku')], max_length=50, blank=True)),
                ('delilnik_kljuc', models.CharField(choices=[('lastniski_delez', 'lastniški delež'), ('povrsina', 'površina enote'), ('st_enot', 'število enot'), ('oseba', 'število oseb')], max_length=50, blank=True)),
                ('is_strosek_posameznidel', models.NullBooleanField(verbose_name='strosek na posameznem delu')),
                ('delovni_nalog', models.OneToOneField(null=True, blank=True, to='delovninalogi.DelovniNalog')),
                ('lastniska_skupina', models.ForeignKey(null=True, blank=True, to='etaznalastnina.LastniskaSkupina')),
                ('obdobje_obracuna_leto', models.ForeignKey(to='core.ObdobjeLeto')),
                ('obdobje_obracuna_mesec', models.ForeignKey(to='core.ObdobjeMesec')),
                ('racun', models.ForeignKey(to='racunovodstvo.Racun')),
            ],
            options={
                'verbose_name_plural': 'stroški',
                'verbose_name': 'strošek',
                'ordering': ('oznaka',),
            },
        ),
        migrations.CreateModel(
            name='VrstaStroska',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('oznaka', models.CharField(unique=True, max_length=20)),
                ('naziv', models.CharField(max_length=200)),
                ('zap_st', models.IntegerField(default=0, verbose_name='zaporedna Številka')),
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
