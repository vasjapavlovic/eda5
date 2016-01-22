# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('deli', '0002_auto_20151215_1854'),
        ('partnerji', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delilnik',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('oznaka', models.CharField(max_length=20)),
                ('meritev', models.IntegerField(choices=[(1, 'Toplota'), (2, 'Hlad'), (3, 'Topla voda'), (4, 'Hladna voda'), (5, 'Elektrika')])),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('datum_odcitka', models.DateField()),
                ('stanje_staro', models.DecimalField(max_digits=15, decimal_places=3)),
                ('stanje_novo', models.DecimalField(max_digits=15, decimal_places=3)),
                ('delilnik', models.ForeignKey(to='stevcnostanje.Delilnik')),
                ('obdobje_leto', models.ForeignKey(to='core.ObdobjeLeto')),
                ('obdobje_mesec', models.ForeignKey(to='core.ObdobjeMesec')),
                ('odcital', models.ForeignKey(to='partnerji.Oseba', blank=True, null=True, verbose_name='odčital')),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('oznaka', models.CharField(max_length=13)),
                ('naziv', models.CharField(max_length=255)),
                ('is_distribucija', models.BooleanField(verbose_name='distribucijski števec')),
                ('del_stavbe', models.ForeignKey(to='deli.DelStavbe', blank=True, null=True)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
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
    ]
