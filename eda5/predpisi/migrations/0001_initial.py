# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Predpis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('oznaka', models.CharField(unique=True, max_length=25)),
                ('naziv', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'predpis',
                'verbose_name_plural': 'predpisi',
            },
        ),
        migrations.CreateModel(
            name='PredpisOpravilo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('oznaka', models.CharField(unique=True, max_length=25)),
                ('naziv', models.CharField(max_length=255)),
                ('predpis', models.ManyToManyField(to='predpisi.Predpis', blank=True)),
            ],
            options={
                'verbose_name': 'predpisano opravilo',
                'verbose_name_plural': 'predpisana opravila',
            },
        ),
        migrations.CreateModel(
            name='PredpisPodsklop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('oznaka', models.CharField(unique=True, max_length=25)),
                ('naziv', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'podsklop predpisov',
                'verbose_name_plural': 'podsklopi predpisov',
            },
        ),
        migrations.CreateModel(
            name='PredpisSklop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('zap_st', models.IntegerField(verbose_name='zaporedna številka', default=9999)),
                ('oznaka', models.CharField(unique=True, max_length=25)),
                ('naziv', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'sklop predpisov',
                'verbose_name_plural': 'sklopi predpisov',
                'ordering': ('zap_st',),
            },
        ),
        migrations.AddField(
            model_name='predpispodsklop',
            name='predpis_sklop',
            field=models.ForeignKey(to='predpisi.PredpisSklop', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='predpisopravilo',
            name='predpis_podsklop',
            field=models.ForeignKey(to='predpisi.PredpisPodsklop', null=True, blank=True),
        ),
    ]
