# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0001_initial'),
        ('deli', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delilnik',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('meritev', models.IntegerField(choices=[(1, 'Toplota'), (2, 'Hlad'), (3, 'Topla voda'), (4, 'Hladna voda'), (5, 'Elektrika')])),
            ],
            options={
                'verbose_name': 'delilnik',
                'ordering': ('stevec',),
                'verbose_name_plural': 'delilniki',
            },
        ),
        migrations.CreateModel(
            name='Odcitek',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('datum_odcitka', models.DateField()),
                ('stanje_staro', models.DecimalField(decimal_places=3, max_digits=15)),
                ('stanje_novo', models.DecimalField(decimal_places=3, max_digits=15)),
                ('delilnik', models.ForeignKey(to='stevci.Delilnik')),
                ('obdobje_leto', models.ForeignKey(to='core.ObdobjeLeto')),
                ('obdobje_mesec', models.ForeignKey(to='core.ObdobjeMesec')),
                ('odcital', models.ForeignKey(to='partnerji.Oseba', verbose_name='odčital', null=True, blank=True)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('oznaka', models.CharField(max_length=13)),
                ('naziv', models.CharField(max_length=255)),
                ('is_distribucija', models.BooleanField(verbose_name='distribucijski števec')),
                ('del_stavbe', models.ForeignKey(to='deli.DelStavbe', null=True, blank=True)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('v_okvari', models.BooleanField()),
                ('v_delovanju', models.BooleanField()),
                ('stevec', models.ForeignKey(to='stevci.Stevec')),
            ],
            options={
                'verbose_name': 'status števca',
                'ordering': ('updated',),
                'verbose_name_plural': 'status števcev',
            },
        ),
        migrations.AddField(
            model_name='delilnik',
            name='stevec',
            field=models.ForeignKey(to='stevci.Stevec'),
        ),
    ]
