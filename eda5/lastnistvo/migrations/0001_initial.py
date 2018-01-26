# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '0001_initial'),
        ('arhiv', '0001_initial'),
        ('etaznalastnina', '0001_initial'),
        ('partnerji', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NajemLastnine',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_likvidiran', models.BooleanField(default=False)),
                ('opombe', models.TextField(blank=True, null=True)),
                ('predaja_datum', models.DateField()),
                ('veljavnost_datum', models.DateField(blank=True, null=True)),
                ('veljavnost_trajanje_opisno', models.CharField(blank=True, max_length=255, null=True, verbose_name='trajanje pogodbe - opisno')),
                ('vracilo_datum', models.DateField(blank=True, null=True)),
                ('vracilo_posebnosti', models.CharField(blank=True, max_length=255, null=True)),
                ('lastniska_enota', models.ForeignKey(null=True, verbose_name='LE', blank=True, to='etaznalastnina.LastniskaEnotaInterna')),
                ('najemna_pogodba', models.ForeignKey(related_name='najemna_pogodba', null=True, blank=True, to='arhiv.Arhiviranje')),
                ('placnik', models.ForeignKey(to='partnerji.Partner')),
            ],
            options={
                'verbose_name_plural': 'najem lastnine',
                'verbose_name': 'najem lastnine',
            },
        ),
        migrations.CreateModel(
            name='PredajaLastnine',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('oznaka', models.CharField(max_length=20, unique=True)),
                ('kupec', models.ForeignKey(to='partnerji.Partner', related_name='kupec')),
                ('prodajalec', models.ForeignKey(to='partnerji.Partner', related_name='prodajalec')),
                ('zahtevek', models.OneToOneField(null=True, blank=True, to='zahtevki.Zahtevek')),
            ],
            options={
                'verbose_name_plural': 'predaje lastnine',
                'verbose_name': 'predaja lastnine',
            },
        ),
        migrations.CreateModel(
            name='ProdajaLastnine',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_likvidiran', models.BooleanField(default=False)),
                ('opombe', models.TextField(blank=True, null=True)),
                ('datum_predaje', models.DateField()),
                ('lastniska_enota', models.ForeignKey(null=True, verbose_name='LE', blank=True, to='etaznalastnina.LastniskaEnotaElaborat')),
                ('placnik', models.ForeignKey(to='partnerji.Partner')),
                ('predaja_lastnine', models.ForeignKey(to='lastnistvo.PredajaLastnine')),
                ('zapisnik_izrocitev', models.ForeignKey(related_name='prodaja_izrocitev_zapisnik', null=True, blank=True, to='arhiv.Arhiviranje')),
            ],
            options={
                'verbose_name_plural': 'prodaja lastnine',
                'verbose_name': 'prodaja lastnine',
            },
        ),
        migrations.AddField(
            model_name='najemlastnine',
            name='predaja_lastnine',
            field=models.ForeignKey(to='lastnistvo.PredajaLastnine'),
        ),
        migrations.AddField(
            model_name='najemlastnine',
            name='vracilo_zapisnik',
            field=models.ForeignKey(related_name='najem_vracilo_zapisnik', null=True, blank=True, to='arhiv.Arhiviranje'),
        ),
        migrations.AddField(
            model_name='najemlastnine',
            name='zapisnik_izrocitev',
            field=models.ForeignKey(related_name='najem_izrocitev_zapisnik', null=True, blank=True, to='arhiv.Arhiviranje'),
        ),
    ]
