# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import eda5.deli.models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DelStavbe',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('shema', models.FileField(blank=True, upload_to=eda5.deli.models.DelStavbe.shema_directory_path, verbose_name='shema sistema')),
            ],
            options={
                'verbose_name_plural': 'deli stavbe',
                'verbose_name': 'del stavbe',
                'ordering': ['oznaka'],
            },
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('tovarniska_st', models.CharField(blank=True, max_length=100, verbose_name='Tovarniška Številka')),
                ('serijska_st', models.CharField(blank=True, max_length=100, verbose_name='Serijska Številka')),
                ('artikel', models.ForeignKey(to='katalog.ModelArtikla', blank=True, null=True, verbose_name='Model')),
            ],
            options={
                'verbose_name_plural': 'elementi',
                'verbose_name': 'element',
            },
        ),
        migrations.CreateModel(
            name='Nastavitev',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('datum_nastavitve', models.DateField()),
                ('vrednost', models.CharField(max_length=20)),
                ('element', models.ForeignKey(to='deli.Element')),
                ('obratovalni_parameter', models.ForeignKey(to='katalog.ObratovalniParameter')),
            ],
            options={
                'verbose_name_plural': 'nastavitve',
                'verbose_name': 'nastavitev',
            },
        ),
        migrations.CreateModel(
            name='Podskupina',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('oznaka', models.CharField(max_length=20, unique=True)),
                ('naziv', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'podskupine delov',
                'verbose_name': 'podskupina delov',
                'ordering': ['oznaka'],
            },
        ),
        migrations.CreateModel(
            name='ProjektnoMesto',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('funkcija', models.CharField(max_length=255)),
                ('del_stavbe', models.ForeignKey(to='deli.DelStavbe')),
                ('tip_elementa', models.ForeignKey(to='katalog.TipArtikla')),
            ],
            options={
                'verbose_name_plural': 'projektna mesta',
                'verbose_name': 'projektno mesto',
                'ordering': ['oznaka'],
            },
        ),
        migrations.CreateModel(
            name='Skupina',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('oznaka', models.CharField(max_length=20, unique=True)),
                ('naziv', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'skupine delov',
                'verbose_name': 'skupina delov',
                'ordering': ['oznaka'],
            },
        ),
        migrations.AddField(
            model_name='podskupina',
            name='skupina',
            field=models.ForeignKey(to='deli.Skupina'),
        ),
        migrations.AddField(
            model_name='element',
            name='projektno_mesto',
            field=models.ForeignKey(to='deli.ProjektnoMesto'),
        ),
    ]
