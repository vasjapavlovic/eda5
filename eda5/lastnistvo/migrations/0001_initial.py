# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etaznalastnina', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NajemLastnine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_likvidiran', models.BooleanField(default=False)),
                ('opombe', models.TextField(null=True, blank=True)),
                ('predaja_datum', models.DateField()),
                ('veljavnost_datum', models.DateField(null=True, blank=True)),
                ('veljavnost_trajanje_opisno', models.CharField(verbose_name='trajanje pogodbe - opisno', max_length=255, null=True, blank=True)),
                ('vracilo_datum', models.DateField(null=True, blank=True)),
                ('vracilo_posebnosti', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'najem lastnine',
                'verbose_name_plural': 'najem lastnine',
            },
        ),
        migrations.CreateModel(
            name='PredajaLastnine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('oznaka', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'verbose_name': 'predaja lastnine',
                'verbose_name_plural': 'predaje lastnine',
            },
        ),
        migrations.CreateModel(
            name='ProdajaLastnine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_likvidiran', models.BooleanField(default=False)),
                ('opombe', models.TextField(null=True, blank=True)),
                ('datum_predaje', models.DateField()),
                ('lastniska_enota', models.ForeignKey(null=True, blank=True, verbose_name='LE', to='etaznalastnina.LastniskaEnotaElaborat')),
            ],
            options={
                'verbose_name': 'prodaja lastnine',
                'verbose_name_plural': 'prodaja lastnine',
            },
        ),
    ]
