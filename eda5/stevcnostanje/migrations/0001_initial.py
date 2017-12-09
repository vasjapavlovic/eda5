# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0001_initial'),
        ('core', '__first__'),
        ('partnerji', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delilnik',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('oznaka', models.CharField(unique=True, max_length=20)),
                ('naziv', models.CharField(null=True, blank=True, max_length=255)),
                ('meritev', models.IntegerField(choices=[(1, 'Toplota [MWh]'), (2, 'Hlad [MWh]'), (3, 'Topla voda [m3]'), (4, 'Hladna voda [m3]'), (5, 'Elektrika [kWh]')])),
                ('opis', models.CharField(null=True, blank=True, max_length=255)),
            ],
            options={
                'verbose_name': 'delilnik',
                'ordering': ('stevec',),
                'verbose_name_plural': 'delilniki',
            },
        ),
        migrations.CreateModel(
            name='MeritevVrsta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('zap_st', models.IntegerField(default=9999, verbose_name='zaporedna številka')),
                ('oznaka', models.CharField(unique=True, max_length=13)),
                ('naziv', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'vrsta meritve',
                'ordering': ('zap_st',),
                'verbose_name_plural': 'vrste meritev',
            },
        ),
        migrations.CreateModel(
            name='Odcitek',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('datum_odcitka', models.DateField()),
                ('stanje_staro', models.DecimalField(max_digits=15, decimal_places=3)),
                ('stanje_novo', models.DecimalField(max_digits=15, decimal_places=3)),
                ('delilnik', models.ForeignKey(to='stevcnostanje.Delilnik')),
                ('obdobje_leto', models.ForeignKey(to='core.ObdobjeLeto')),
                ('obdobje_mesec', models.ForeignKey(to='core.ObdobjeMesec')),
                ('odcital', models.ForeignKey(null=True, verbose_name='odčital', blank=True, to='partnerji.Oseba')),
            ],
            options={
                'ordering': ('delilnik', 'datum_odcitka'),
                'verbose_name': 'odcitek',
                'verbose_name_plural': 'odcitki',
            },
        ),
        migrations.CreateModel(
            name='Stevec',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('oznaka', models.CharField(unique=True, max_length=13)),
                ('naziv', models.CharField(max_length=255)),
                ('is_distribucija', models.BooleanField(verbose_name='distribucijski števec')),
                ('projektno_mesto', models.ForeignKey(null=True, blank=True, to='deli.ProjektnoMesto')),
                ('upravljavec', models.ForeignKey(to='partnerji.Partner')),
            ],
            options={
                'verbose_name': 'števec',
                'ordering': ('oznaka',),
                'verbose_name_plural': 'števci',
            },
        ),
        migrations.CreateModel(
            name='StevecStatus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('v_okvari', models.BooleanField()),
                ('v_delovanju', models.BooleanField()),
                ('stevec', models.ForeignKey(to='stevcnostanje.Stevec')),
            ],
            options={
                'verbose_name': 'status števca',
                'ordering': ('updated',),
                'verbose_name_plural': 'status števcev',
            },
        ),
        migrations.AddField(
            model_name='delilnik',
            name='meritev_vrsta',
            field=models.ForeignKey(null=True, blank=True, to='stevcnostanje.MeritevVrsta'),
        ),
        migrations.AddField(
            model_name='delilnik',
            name='stevec',
            field=models.ForeignKey(to='stevcnostanje.Stevec'),
        ),
        migrations.AlterUniqueTogether(
            name='odcitek',
            unique_together=set([('delilnik', 'obdobje_leto', 'obdobje_mesec')]),
        ),
    ]
