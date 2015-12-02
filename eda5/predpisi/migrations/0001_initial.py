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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=25)),
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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=25)),
                ('naziv', models.CharField(max_length=255)),
                ('predpis', models.ManyToManyField(to='predpisi.Predpis')),
            ],
            options={
                'verbose_name_plural': 'predpisi',
                'verbose_name': 'predpis',
            },
        ),
        migrations.CreateModel(
            name='PredpisPodsklop',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=25)),
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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=25)),
                ('naziv', models.CharField(max_length=255)),
                ('zap_st', models.IntegerField(default=0, verbose_name='zaporedna številka')),
            ],
            options={
                'verbose_name_plural': 'sklopi predpisov',
                'ordering': ('zap_st',),
                'verbose_name': 'sklop predpisov',
            },
        ),
        migrations.AddField(
            model_name='predpispodsklop',
            name='predpis_sklop',
            field=models.ForeignKey(to='predpisi.PredpisSklop'),
        ),
        migrations.AddField(
            model_name='predpis',
            name='predpis_podsklop',
            field=models.ForeignKey(to='predpisi.PredpisPodsklop'),
        ),
    ]
