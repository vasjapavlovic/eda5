# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0001_initial'),
        ('narocila', '0001_initial'),
        ('etaznalastnina', '0001_initial'),
        ('delovninalogi', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Konto',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('oznaka', models.CharField(max_length=10, unique=True)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('oznaka', models.CharField(max_length=10, unique=True)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_likvidiran', models.BooleanField(default=False)),
                ('davcna_klasifikacija', models.IntegerField(choices=[(0, 'podjetje'), (1, 'razdelilnik')])),
                ('datum_storitve_od', models.DateField()),
                ('datum_storitve_do', models.DateField()),
                ('osnova_0', models.DecimalField(max_digits=7, blank=True, decimal_places=2, null=True, verbose_name='osnova brez ddv')),
                ('osnova_1', models.DecimalField(max_digits=7, blank=True, decimal_places=2, null=True, verbose_name='osnova nižja stopnja')),
                ('osnova_2', models.DecimalField(max_digits=7, blank=True, decimal_places=2, null=True, verbose_name='osnova višja stopnja')),
                ('dokument', models.ForeignKey(to='posta.Dokument', blank=True, null=True)),
                ('narocilo', models.ForeignKey(to='narocila.Narocilo', blank=True, null=True)),
                ('obdobje_obracuna_leto', models.ForeignKey(to='core.ObdobjeLeto')),
                ('obdobje_obracuna_mesec', models.ForeignKey(to='core.ObdobjeMesec')),
            ],
            options={
                'verbose_name_plural': 'računi',
                'verbose_name': 'račun',
            },
        ),
        migrations.CreateModel(
            name='SkupinaVrsteStroska',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('oznaka', models.CharField(max_length=20, unique=True)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=200)),
                ('datum_storitve_od', models.DateField()),
                ('datum_storitve_do', models.DateField()),
                ('osnova', models.DecimalField(max_digits=7, decimal_places=2, verbose_name='osnova za ddv')),
                ('stopnja_ddv', models.IntegerField(choices=[(0, 'neobdavčeno'), (1, 'nižja stopnja'), (2, 'višja stopnja')], verbose_name='stopnja DDV')),
                ('delilnik_vrsta', models.CharField(choices=[('fiksni', 'fiksni strošek'), ('vuporabi', 'LE v uporabi'), ('delilniki', 'po priloženem delilniku')], max_length=50)),
                ('delilnik_kljuc', models.CharField(choices=[('lastniski_delez', 'lastniški delež'), ('povrsina', 'površina enote'), ('st_enot', 'število enot'), ('oseba', 'število oseb')], max_length=50)),
                ('is_strosek_posameznidel', models.BooleanField(verbose_name='strosek na posameznem delu')),
                ('delovni_nalog', models.OneToOneField(to='delovninalogi.DelovniNalog', blank=True, null=True)),
                ('lastniska_skupina', models.ForeignKey(to='etaznalastnina.LastniskaSkupina', blank=True, null=True)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('oznaka', models.CharField(max_length=20, unique=True)),
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
