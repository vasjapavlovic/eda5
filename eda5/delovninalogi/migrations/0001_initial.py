# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('narocila', '0001_initial'),
        ('partnerji', '0001_initial'),
        ('zahtevki', '0001_initial'),
        ('deli', '0001_initial'),
        ('posta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno')], default=0)),
                ('datum', models.DateField(blank=True, null=True)),
                ('time_start', models.TimeField(verbose_name='Ura:Začeto', blank=True, null=True)),
                ('time_stop', models.TimeField(verbose_name='Ura:Končano', blank=True, null=True)),
                ('delavec', models.ForeignKey(to='partnerji.Oseba')),
            ],
            options={
                'verbose_name': 'Delo',
                'verbose_name_plural': 'Dela',
            },
        ),
        migrations.CreateModel(
            name='DelovniNalog',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno')], default=0)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('datum_plan', models.DateField(verbose_name='V planu za dne', blank=True, null=True)),
                ('datum_start', models.DateField(verbose_name='Začeto dne', blank=True, null=True)),
                ('datum_stop', models.DateField(verbose_name='Končano dne', blank=True, null=True)),
                ('dokument', models.ManyToManyField(to='posta.Dokument', blank=True)),
                ('nosilec', models.ForeignKey(to='partnerji.Oseba')),
            ],
            options={
                'verbose_name': 'Delovni Nalog',
                'verbose_name_plural': 'Delovni Nalogi',
            },
        ),
        migrations.CreateModel(
            name='Opravilo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('rok_izvedbe', models.DateField()),
                ('is_potrjen', models.BooleanField(verbose_name='Potrjeno iz strani nadzornika', default=False)),
                ('element', models.ManyToManyField(to='deli.Element')),
                ('nadzornik', models.ForeignKey(to='partnerji.Oseba')),
                ('narocilo', models.ForeignKey(verbose_name='naročilo', to='narocila.Narocilo')),
                ('zahtevek', models.ForeignKey(to='zahtevki.Zahtevek')),
            ],
            options={
                'verbose_name': 'Opravilo',
                'verbose_name_plural': 'Opravila',
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
