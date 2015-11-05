# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0007_auto_20151030_1131'),
        ('core', '0001_initial'),
        ('partnerji', '0013_auto_20151030_1310'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delilnik',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=20)),
                ('meritev', models.IntegerField(choices=[(1, 'Toplota'), (2, 'Hlad'), (3, 'Topla voda'), (4, 'Hladna voda'), (5, 'Elektrika')])),
            ],
            options={
                'verbose_name_plural': 'delilniki',
                'ordering': ('stevec',),
                'verbose_name': 'delilnik',
            },
        ),
        migrations.CreateModel(
            name='Odcitek',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('datum_odcitka', models.DateField()),
                ('stanje_staro', models.DecimalField(max_digits=15, decimal_places=3)),
                ('stanje_novo', models.DecimalField(max_digits=15, decimal_places=3)),
                ('delilnik', models.ForeignKey(to='stevci.Delilnik')),
                ('obdobje_leto', models.ForeignKey(to='core.ObdobjeLeto')),
                ('obdobje_mesec', models.ForeignKey(to='core.ObdobjeMesec')),
            ],
            options={
                'verbose_name_plural': 'odcitki',
                'ordering': ('delilnik', 'datum_odcitka'),
                'verbose_name': 'odcitek',
            },
        ),
        migrations.CreateModel(
            name='Stevec',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=13)),
                ('naziv', models.CharField(max_length=255)),
                ('is_distribucija', models.BooleanField(verbose_name='distribucijski števec')),
                ('del_stavbe', models.ForeignKey(to='deli.DelStavbe')),
                ('upravljavec', models.ForeignKey(to='partnerji.Partner')),
            ],
            options={
                'verbose_name_plural': 'števci',
                'ordering': ('oznaka',),
                'verbose_name': 'števec',
            },
        ),
        migrations.CreateModel(
            name='StevecStatus',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('v_okvari', models.BooleanField()),
                ('v_delovanju', models.BooleanField()),
                ('stevec', models.ForeignKey(to='stevci.Stevec')),
            ],
            options={
                'verbose_name_plural': 'status števcev',
                'ordering': ('updated',),
                'verbose_name': 'status števca',
            },
        ),
        migrations.AddField(
            model_name='delilnik',
            name='stevec',
            field=models.ForeignKey(to='stevci.Stevec'),
        ),
    ]
