# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DelStavbe',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('oznaka', models.CharField(max_length=50, unique=True)),
                ('naziv', models.CharField(max_length=255)),
                ('funkcija', models.CharField(max_length=255, blank=True, null=True, verbose_name='funkcija sistema')),
                ('bim_id', models.CharField(max_length=100, blank=True, null=True, verbose_name='BIM ID')),
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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('tovarniska_st', models.CharField(max_length=100, blank=True, verbose_name='Tovarniška Številka')),
                ('serijska_st', models.CharField(max_length=100, blank=True, verbose_name='Serijska Številka')),
            ],
            options={
                'verbose_name_plural': 'elementi',
                'verbose_name': 'element',
            },
        ),
        migrations.CreateModel(
            name='Etaza',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('oznaka', models.CharField(max_length=50, verbose_name='Oznaka', unique=True)),
                ('naziv', models.CharField(max_length=255, blank=True, null=True, verbose_name='Naziv')),
                ('opis', models.TextField(blank=True, null=True, verbose_name='Opis')),
                ('elevation', models.DecimalField(max_digits=20, blank=True, null=True, decimal_places=5, verbose_name='Višinska kota Etaže')),
            ],
            options={
                'verbose_name_plural': 'Etaže',
                'verbose_name': 'Etaža',
                'ordering': ['oznaka'],
            },
        ),
        migrations.CreateModel(
            name='Lokacija',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Lokacije',
                'verbose_name': 'Lokacija',
                'ordering': ['prostor__oznaka'],
            },
        ),
        migrations.CreateModel(
            name='Nastavitev',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('datum_nastavitve', models.DateField()),
                ('vrednost', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'nastavitve',
                'verbose_name': 'nastavitev',
            },
        ),
        migrations.CreateModel(
            name='Podskupina',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('oznaka', models.CharField(max_length=20, verbose_name='Oznaka', unique=True)),
                ('naziv', models.CharField(max_length=255, verbose_name='Naziv')),
                ('funkcija', models.CharField(max_length=255, blank=True, null=True, verbose_name='Funkcija Elementa')),
                ('bim_id', models.CharField(max_length=100, blank=True, null=True, verbose_name='BIM ID')),
                ('del_stavbe', models.ForeignKey(to='deli.DelStavbe', verbose_name='Del Stavbe')),
                ('lokacija', models.ForeignKey(to='deli.Lokacija', verbose_name='Lokacija v Stavbi', blank=True, null=True)),
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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('oznaka', models.CharField(max_length=20, unique=True)),
                ('naziv', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'skupine delov',
                'verbose_name': 'skupina delov',
                'ordering': ['oznaka'],
            },
        ),
        migrations.CreateModel(
            name='Stavba',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('oznaka', models.CharField(max_length=20, verbose_name='Oznaka', unique=True)),
                ('naziv', models.CharField(max_length=255, blank=True, null=True, verbose_name='Naziv')),
                ('opis', models.TextField(blank=True, null=True, verbose_name='Opis')),
            ],
            options={
                'verbose_name_plural': 'Stavbe',
                'verbose_name': 'Stavba',
                'ordering': ['oznaka'],
            },
        ),
    ]
