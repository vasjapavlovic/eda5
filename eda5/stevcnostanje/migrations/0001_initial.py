# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0001_initial'),
        ('core', '0001_initial'),
        ('partnerji', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delilnik',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=20, unique=True)),
                ('naziv', models.CharField(blank=True, max_length=255, null=True)),
                ('meritev', models.IntegerField(choices=[(1, 'Toplota [MWh]'), (2, 'Hlad [MWh]'), (3, 'Topla voda [m3]'), (4, 'Hladna voda [m3]'), (5, 'Elektrika [kWh]')])),
                ('opis', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'delilniki',
                'verbose_name': 'delilnik',
                'ordering': ('stevec',),
            },
        ),
        migrations.CreateModel(
            name='MeritevVrsta',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('zap_st', models.IntegerField(verbose_name='zaporedna številka', default=9999)),
                ('oznaka', models.CharField(max_length=13, unique=True)),
                ('naziv', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'vrste meritev',
                'verbose_name': 'vrsta meritve',
                'ordering': ('zap_st',),
            },
        ),
        migrations.CreateModel(
            name='Odcitek',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('datum_odcitka', models.DateField()),
                ('stanje_staro', models.DecimalField(max_digits=15, decimal_places=3)),
                ('stanje_novo', models.DecimalField(max_digits=15, decimal_places=3)),
                ('delilnik', models.ForeignKey(to='stevcnostanje.Delilnik')),
                ('obdobje_leto', models.ForeignKey(to='core.ObdobjeLeto')),
                ('obdobje_mesec', models.ForeignKey(to='core.ObdobjeMesec')),
                ('odcital', models.ForeignKey(null=True, verbose_name='odčital', blank=True, to='partnerji.Oseba')),
            ],
            options={
                'verbose_name_plural': 'odcitki',
                'verbose_name': 'odcitek',
                'ordering': ('delilnik', 'datum_odcitka'),
            },
        ),
        migrations.CreateModel(
            name='Stevec',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=13, unique=True)),
                ('naziv', models.CharField(max_length=255)),
                ('is_distribucija', models.BooleanField(verbose_name='distribucijski števec')),
                ('projektno_mesto', models.ForeignKey(null=True, blank=True, to='deli.ProjektnoMesto')),
                ('upravljavec', models.ForeignKey(to='partnerji.Partner')),
            ],
            options={
                'verbose_name_plural': 'števci',
                'verbose_name': 'števec',
                'ordering': ('oznaka',),
            },
        ),
        migrations.CreateModel(
            name='StevecStatus',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('v_okvari', models.BooleanField()),
                ('v_delovanju', models.BooleanField()),
                ('stevec', models.ForeignKey(to='stevcnostanje.Stevec')),
            ],
            options={
                'verbose_name_plural': 'status števcev',
                'verbose_name': 'status števca',
                'ordering': ('updated',),
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
