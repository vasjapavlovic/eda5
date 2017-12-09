# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0001_initial'),
        ('etaznalastnina', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='DelStavbe',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('oznaka', models.CharField(unique=True, max_length=50)),
                ('naziv', models.CharField(max_length=255)),
                ('funkcija', models.CharField(null=True, verbose_name='funkcija sistema', blank=True, max_length=255)),
                ('bim_id', models.CharField(null=True, verbose_name='BIM ID', blank=True, max_length=100)),
                ('lastniska_skupina', models.ForeignKey(null=True, verbose_name='lastniška skupina', blank=True, to='etaznalastnina.LastniskaSkupina')),
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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('tovarniska_st', models.CharField(verbose_name='Tovarniška Številka', blank=True, max_length=100)),
                ('serijska_st', models.CharField(verbose_name='Serijska Številka', blank=True, max_length=100)),
                ('artikel', models.ForeignKey(null=True, verbose_name='Model', blank=True, to='katalog.ModelArtikla')),
            ],
            options={
                'verbose_name': 'element',
                'verbose_name_plural': 'elementi',
            },
        ),
        migrations.CreateModel(
            name='Etaza',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('oznaka', models.CharField(verbose_name='Oznaka', unique=True, max_length=50)),
                ('naziv', models.CharField(null=True, verbose_name='Naziv', blank=True, max_length=255)),
                ('opis', models.TextField(null=True, verbose_name='Opis', blank=True)),
                ('elevation', models.DecimalField(null=True, verbose_name='Višinska kota Etaže', blank=True, decimal_places=5, max_digits=20)),
            ],
            options={
                'verbose_name': 'Etaža',
                'ordering': ['oznaka'],
                'verbose_name_plural': 'Etaže',
            },
        ),
        migrations.CreateModel(
            name='Lokacija',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('etaza', models.ForeignKey(verbose_name='Etaža', to='deli.Etaza')),
                ('prostor', models.OneToOneField(verbose_name='Prostor', to='deli.DelStavbe')),
            ],
            options={
                'verbose_name': 'Lokacija',
                'ordering': ['prostor__oznaka'],
                'verbose_name_plural': 'Lokacije',
            },
        ),
        migrations.CreateModel(
            name='Nastavitev',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('oznaka', models.CharField(unique=True, max_length=20)),
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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('oznaka', models.CharField(verbose_name='Oznaka', unique=True, max_length=20)),
                ('naziv', models.CharField(verbose_name='Naziv', max_length=255)),
                ('funkcija', models.CharField(null=True, verbose_name='Funkcija Elementa', blank=True, max_length=255)),
                ('bim_id', models.CharField(null=True, verbose_name='BIM ID', blank=True, max_length=100)),
                ('del_stavbe', models.ForeignKey(verbose_name='Del Stavbe', to='deli.DelStavbe')),
                ('lokacija', models.ForeignKey(null=True, verbose_name='Lokacija v Stavbi', blank=True, to='deli.Lokacija')),
                ('tip_elementa', models.ForeignKey(null=True, verbose_name='Tip Elementa', blank=True, to='katalog.TipArtikla')),
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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('oznaka', models.CharField(unique=True, max_length=20)),
                ('naziv', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'skupina delov',
                'ordering': ['oznaka'],
                'verbose_name_plural': 'skupine delov',
            },
        ),
        migrations.CreateModel(
            name='Stavba',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('oznaka', models.CharField(verbose_name='Oznaka', unique=True, max_length=20)),
                ('naziv', models.CharField(null=True, verbose_name='Naziv', blank=True, max_length=255)),
                ('opis', models.TextField(null=True, verbose_name='Opis', blank=True)),
            ],
            options={
                'verbose_name': 'Stavba',
                'ordering': ['oznaka'],
                'verbose_name_plural': 'Stavbe',
            },
        ),
        migrations.AddField(
            model_name='podskupina',
            name='skupina',
            field=models.ForeignKey(to='deli.Skupina'),
        ),
        migrations.AddField(
            model_name='etaza',
            name='stavba',
            field=models.ForeignKey(verbose_name='Stavba', to='deli.Stavba'),
        ),
        migrations.AddField(
            model_name='element',
            name='projektno_mesto',
            field=models.ForeignKey(verbose_name='projektno mesto', to='deli.ProjektnoMesto'),
        ),
        migrations.AddField(
            model_name='delstavbe',
            name='podskupina',
            field=models.ForeignKey(to='deli.Podskupina'),
        ),
    ]
