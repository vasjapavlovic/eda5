# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delovninalogi', '0001_initial'),
        ('etaznalastnina', '0001_initial'),
        ('posta', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DavcnaKlasifikacija',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('oznaka', models.CharField(max_length=10)),
                ('naziv', models.CharField(max_length=50)),
                ('opis', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'davčna klasifikacija',
                'verbose_name_plural': 'davčna klasifikacija',
            },
        ),
        migrations.CreateModel(
            name='Konto',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('oznaka', models.CharField(max_length=10)),
                ('naziv', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'konto',
                'ordering': ('oznaka',),
                'verbose_name_plural': 'konti',
            },
        ),
        migrations.CreateModel(
            name='PodKonto',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('oznaka', models.CharField(max_length=10)),
                ('naziv', models.CharField(max_length=50)),
                ('zap_st', models.IntegerField(verbose_name='zaporedna Številka', default=0)),
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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_likvidiran', models.BooleanField(default=False)),
                ('datum_storitve_od', models.DateField()),
                ('datum_storitve_do', models.DateField()),
                ('davcna_klasifikacija', models.ForeignKey(to='racunovodstvo.DavcnaKlasifikacija')),
                ('dokument', models.ForeignKey(to='posta.Dokument')),
                ('obdobje_obracuna_leto', models.ForeignKey(to='core.ObdobjeLeto')),
                ('obdobje_obracuna_mesec', models.ForeignKey(to='core.ObdobjeMesec')),
            ],
            options={
                'verbose_name': 'račun',
                'verbose_name_plural': 'računi',
            },
        ),
        migrations.CreateModel(
            name='SkupinaVrsteStroska',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=200)),
                ('zap_st', models.IntegerField(verbose_name='zaporedna Številka', default=0)),
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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=200)),
                ('datum_storitve_od', models.DateField()),
                ('datum_storitve_do', models.DateField()),
                ('vrednost', models.DecimalField(max_digits=7, decimal_places=2)),
                ('stopnja_ddv', models.DecimalField(max_digits=4, decimal_places=3)),
                ('delilnik_vrsta', models.CharField(choices=[('fiksni', 'fiksni strošek'), ('vuporabi', 'LE v uporabi'), ('delilniki', 'po priloženem delilniku')], max_length=50)),
                ('delilnik_kljuc', models.CharField(choices=[('lastniski_delez', 'lastniški delež'), ('povrsina', 'površina enote'), ('st_enot', 'število enot'), ('oseba', 'število oseb')], max_length=50)),
                ('is_strosek_posameznidel', models.BooleanField(verbose_name='strosek na posameznem delu')),
                ('delovni_nalog', models.OneToOneField(to='delovninalogi.DelovniNalog', null=True, blank=True)),
                ('lastniska_skupina', models.ForeignKey(to='etaznalastnina.LastniskaSkupina')),
                ('racun', models.ForeignKey(to='racunovodstvo.Racun')),
            ],
            options={
                'verbose_name': 'strošek',
                'ordering': ('oznaka',),
                'verbose_name_plural': 'stroški',
            },
        ),
        migrations.CreateModel(
            name='VrstaStroska',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=200)),
                ('zap_st', models.IntegerField(verbose_name='zaporedna Številka', default=0)),
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
