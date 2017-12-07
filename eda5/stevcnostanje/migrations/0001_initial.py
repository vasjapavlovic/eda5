# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '__first__'),
        ('core', '__first__'),
        ('deli', '0002_auto_20170822_1750'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delilnik',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('oznaka', models.CharField(max_length=20, unique=True)),
                ('meritev', models.IntegerField(choices=[(1, 'Toplota [MWh]'), (2, 'Hlad [MWh]'), (3, 'Topla voda [m3]'), (4, 'Hladna voda [m3]'), (5, 'Elektrika [kWh]')])),
                ('opis', models.CharField(max_length=255, blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'delilniki',
                'verbose_name': 'delilnik',
                'ordering': ('stevec',),
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
                ('odcital', models.ForeignKey(verbose_name='odčital', blank=True, to='partnerji.Oseba', null=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('oznaka', models.CharField(max_length=13, unique=True)),
                ('naziv', models.CharField(max_length=255)),
                ('is_distribucija', models.BooleanField(verbose_name='distribucijski števec')),
                ('projektno_mesto', models.ForeignKey(blank=True, to='deli.ProjektnoMesto', null=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
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
            name='stevec',
            field=models.ForeignKey(to='stevcnostanje.Stevec'),
        ),
        migrations.AlterUniqueTogether(
            name='odcitek',
            unique_together=set([('delilnik', 'obdobje_leto', 'obdobje_mesec')]),
        ),
    ]
