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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('shema', models.FileField(upload_to=eda5.deli.models.DelStavbe.shema_directory_path, verbose_name='shema sistema', blank=True)),
            ],
            options={
                'verbose_name': 'del stavbe',
                'ordering': ['oznaka'],
                'verbose_name_plural': 'deli stavbe',
            },
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('is_active', models.BooleanField(default=True)),
                ('tovarniska_st', models.CharField(verbose_name='Tovarniška Številka', max_length=100, blank=True)),
                ('serijska_st', models.CharField(verbose_name='Serijska Številka', max_length=100, blank=True)),
                ('artikel', models.ForeignKey(to='katalog.ModelArtikla', null=True, verbose_name='Model', blank=True)),
            ],
            options={
                'verbose_name': 'element',
                'verbose_name_plural': 'elementi',
            },
        ),
        migrations.CreateModel(
            name='Nastavitev',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('datum_nastavitve', models.DateField()),
                ('vrednost', models.CharField(max_length=20)),
                ('element', models.ForeignKey(to='deli.Element')),
                ('obratovalni_parameter', models.ForeignKey(to='katalog.ObratovalniParameter')),
            ],
            options={
                'verbose_name': 'nastavitev',
                'verbose_name_plural': 'nastavitve',
            },
        ),
        migrations.CreateModel(
            name='Podskupina',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'podskupina delov',
                'ordering': ['oznaka'],
                'verbose_name_plural': 'podskupine delov',
            },
        ),
        migrations.CreateModel(
            name='ProjektnoMesto',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('funkcija', models.CharField(max_length=255)),
                ('del_stavbe', models.ForeignKey(to='deli.DelStavbe')),
                ('tip_elementa', models.ForeignKey(to='katalog.TipArtikla')),
            ],
            options={
                'verbose_name': 'projektno mesto',
                'ordering': ['oznaka'],
                'verbose_name_plural': 'projektna mesta',
            },
        ),
        migrations.CreateModel(
            name='Skupina',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'skupina delov',
                'ordering': ['oznaka'],
                'verbose_name_plural': 'skupine delov',
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
