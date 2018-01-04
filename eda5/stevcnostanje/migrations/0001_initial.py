# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0002_auto_20180104_1543'),
        ('core', '0001_initial'),
        ('partnerji', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delilnik',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('oznaka', models.CharField(max_length=20, unique=True)),
                ('naziv', models.CharField(max_length=255, null=True, blank=True)),
                ('meritev', models.IntegerField(choices=[(1, 'Toplota [MWh]'), (2, 'Hlad [MWh]'), (3, 'Topla voda [m3]'), (4, 'Hladna voda [m3]'), (5, 'Elektrika [kWh]')])),
                ('opis', models.CharField(max_length=255, null=True, blank=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('zap_st', models.IntegerField(verbose_name='zaporedna številka', default=9999)),
                ('oznaka', models.CharField(max_length=13, unique=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('datum_odcitka', models.DateField()),
                ('stanje_staro', models.DecimalField(decimal_places=3, max_digits=15)),
                ('stanje_novo', models.DecimalField(decimal_places=3, max_digits=15)),
                ('delilnik', models.ForeignKey(to='stevcnostanje.Delilnik')),
                ('obdobje_leto', models.ForeignKey(to='core.ObdobjeLeto')),
                ('obdobje_mesec', models.ForeignKey(to='core.ObdobjeMesec')),
                ('odcital', models.ForeignKey(null=True, blank=True, verbose_name='odčital', to='partnerji.Oseba')),
            ],
            options={
                'verbose_name': 'odcitek',
                'ordering': ('delilnik', 'datum_odcitka'),
                'verbose_name_plural': 'odcitki',
            },
        ),
        migrations.CreateModel(
            name='Stevec',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('oznaka', models.CharField(max_length=13, unique=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
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
