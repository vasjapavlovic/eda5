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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=25, unique=True)),
                ('naziv', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'predpisi',
                'verbose_name': 'predpis',
            },
        ),
        migrations.CreateModel(
            name='PredpisOpravilo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=25, unique=True)),
                ('naziv', models.CharField(max_length=255)),
                ('predpis', models.ManyToManyField(blank=True, to='predpisi.Predpis')),
            ],
            options={
                'verbose_name_plural': 'predpisana opravila',
                'verbose_name': 'predpisano opravilo',
            },
        ),
        migrations.CreateModel(
            name='PredpisPodsklop',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=25, unique=True)),
                ('naziv', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'podsklopi predpisov',
                'verbose_name': 'podsklop predpisov',
            },
        ),
        migrations.CreateModel(
            name='PredpisSklop',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('zap_st', models.IntegerField(verbose_name='zaporedna številka', default=9999)),
                ('oznaka', models.CharField(max_length=25, unique=True)),
                ('naziv', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'sklopi predpisov',
                'verbose_name': 'sklop predpisov',
                'ordering': ('zap_st',),
            },
        ),
        migrations.AddField(
            model_name='predpispodsklop',
            name='predpis_sklop',
            field=models.ForeignKey(null=True, blank=True, to='predpisi.PredpisSklop'),
        ),
        migrations.AddField(
            model_name='predpisopravilo',
            name='predpis_podsklop',
            field=models.ForeignKey(null=True, blank=True, to='predpisi.PredpisPodsklop'),
        ),
    ]
