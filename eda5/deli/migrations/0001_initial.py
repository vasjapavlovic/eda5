# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0001_initial'),
        ('etaznalastnina', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DelStavbe',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('oznaka', models.CharField(max_length=50, unique=True)),
                ('naziv', models.CharField(max_length=255)),
                ('funkcija', models.CharField(blank=True, max_length=255, null=True, verbose_name='funkcija sistema')),
                ('bim_id', models.CharField(blank=True, max_length=100, null=True, verbose_name='BIM ID')),
                ('lastniska_skupina', models.ForeignKey(null=True, verbose_name='lastniška skupina', blank=True, to='etaznalastnina.LastniskaSkupina')),
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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('tovarniska_st', models.CharField(blank=True, max_length=100, verbose_name='Tovarniška Številka')),
                ('serijska_st', models.CharField(blank=True, max_length=100, verbose_name='Serijska Številka')),
                ('artikel', models.ForeignKey(null=True, verbose_name='Model', blank=True, to='katalog.ModelArtikla')),
            ],
            options={
                'verbose_name_plural': 'elementi',
                'verbose_name': 'element',
            },
        ),
        migrations.CreateModel(
            name='Etaza',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('oznaka', models.CharField(verbose_name='Oznaka', max_length=50, unique=True)),
                ('naziv', models.CharField(blank=True, max_length=255, null=True, verbose_name='Naziv')),
                ('opis', models.TextField(blank=True, null=True, verbose_name='Opis')),
                ('elevation', models.DecimalField(blank=True, max_digits=20, decimal_places=5, null=True, verbose_name='Višinska kota Etaže')),
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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('etaza', models.ForeignKey(verbose_name='Etaža', to='deli.Etaza')),
                ('prostor', models.OneToOneField(verbose_name='Prostor', to='deli.DelStavbe')),
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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('oznaka', models.CharField(verbose_name='Oznaka', max_length=20, unique=True)),
                ('naziv', models.CharField(verbose_name='Naziv', max_length=255)),
                ('funkcija', models.CharField(blank=True, max_length=255, null=True, verbose_name='Funkcija Elementa')),
                ('bim_id', models.CharField(blank=True, max_length=100, null=True, verbose_name='BIM ID')),
                ('del_stavbe', models.ForeignKey(verbose_name='Del Stavbe', to='deli.DelStavbe')),
                ('lokacija', models.ForeignKey(null=True, verbose_name='Lokacija v Stavbi', blank=True, to='deli.Lokacija')),
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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('oznaka', models.CharField(verbose_name='Oznaka', max_length=20, unique=True)),
                ('naziv', models.CharField(blank=True, max_length=255, null=True, verbose_name='Naziv')),
                ('opis', models.TextField(blank=True, null=True, verbose_name='Opis')),
            ],
            options={
                'verbose_name_plural': 'Stavbe',
                'verbose_name': 'Stavba',
                'ordering': ['oznaka'],
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
        migrations.AddField(
            model_name='delstavbe',
            name='stavba',
            field=models.ForeignKey(null=True, blank=True, to='deli.Stavba'),
        ),
    ]
