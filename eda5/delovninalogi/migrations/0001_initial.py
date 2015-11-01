# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0007_auto_20151030_1131'),
        ('zahtevki', '0006_auto_20151101_1518'),
        ('partnerji', '0013_auto_20151030_1310'),
        ('narocila', '0006_auto_20151101_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('datum', models.DateField(null=True, blank=True)),
                ('time_start', models.TimeField(null=True, blank=True, verbose_name='Ura:Končano')),
                ('delavec', models.ForeignKey(to='partnerji.Oseba')),
            ],
            options={
                'verbose_name_plural': 'Dela',
                'verbose_name': 'Delo',
            },
        ),
        migrations.CreateModel(
            name='DelovniNalog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('date_plan', models.DateField(verbose_name='V planu za dne')),
                ('datum_start', models.DateField(null=True, blank=True, verbose_name='Začeto dne')),
                ('datum_stop', models.DateField(null=True, blank=True, verbose_name='Končano dne')),
                ('nosilec', models.ForeignKey(to='partnerji.Oseba')),
            ],
            options={
                'verbose_name_plural': 'Delovni Nalogi',
                'verbose_name': 'Delovni Nalog',
            },
        ),
        migrations.CreateModel(
            name='Opravilo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('rok_izvedbe', models.DateField()),
                ('element', models.ManyToManyField(to='deli.Element')),
                ('narocilo', models.ForeignKey(verbose_name='naročilo', to='narocila.Narocilo')),
                ('zahtevek', models.ForeignKey(to='zahtevki.Zahtevek')),
            ],
            options={
                'verbose_name_plural': 'Opravila',
                'verbose_name': 'Opravilo',
            },
        ),
        migrations.AddField(
            model_name='delovninalog',
            name='opravilo',
            field=models.ForeignKey(to='delovninalogi.Opravilo'),
        ),
        migrations.AddField(
            model_name='delo',
            name='delovninalog',
            field=models.ForeignKey(verbose_name='delovni nalog', to='delovninalogi.DelovniNalog'),
        ),
    ]
