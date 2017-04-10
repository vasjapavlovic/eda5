# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '__first__'),
        ('pomanjkljivosti', '__first__'),
        ('partnerji', '__first__'),
        ('narocila', '__first__'),
        ('zahtevki', '__first__'),
        ('planiranje', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('status', models.IntegerField(choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano')], default=0)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('datum', models.DateField(null=True, blank=True)),
                ('time_start', models.DurationField(null=True, verbose_name='Ura:Začeto', blank=True)),
                ('time_stop', models.DurationField(null=True, verbose_name='Ura:Končano', blank=True)),
                ('delo_cas_rac', models.DecimalField(null=True, verbose_name='Porabljen čas [UR]', blank=True, decimal_places=2, max_digits=5)),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('status', models.IntegerField(choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano')], default=0)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('datum_plan', models.DateField(null=True, verbose_name='V planu za dne', blank=True)),
                ('datum_start', models.DateField(null=True, verbose_name='Začeto dne', blank=True)),
                ('datum_stop', models.DateField(null=True, verbose_name='Končano dne', blank=True)),
                ('nosilec', models.ForeignKey(null=True, blank=True, to='partnerji.Oseba', verbose_name='Izvajalec (kdo bo delo izvedel)')),
            ],
            options={
                'verbose_name': 'Delovni Nalog',
                'verbose_name_plural': 'Delovni Nalogi',
            },
        ),
        migrations.CreateModel(
            name='DeloVrsta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('oznaka', models.CharField(max_length=20, unique=True)),
                ('naziv', models.CharField(max_length=255)),
                ('zap_st', models.IntegerField(default=99)),
                ('cena', models.DecimalField(max_digits=4, decimal_places=2)),
                ('stopnja_ddv', models.DecimalField(max_digits=4, decimal_places=3)),
            ],
            options={
                'verbose_name': 'vrsta dela',
                'verbose_name_plural': 'vrste del',
            },
        ),
        migrations.CreateModel(
            name='DeloVrstaSklop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('oznaka', models.CharField(max_length=20, unique=True)),
                ('naziv', models.CharField(max_length=255)),
                ('zap_st', models.IntegerField(default=99)),
            ],
            options={
                'verbose_name': 'sklop vrst del',
                'verbose_name_plural': 'sklopi vrst del',
            },
        ),
        migrations.CreateModel(
            name='Opravilo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('status', models.IntegerField(choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano')], default=0)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('rok_izvedbe', models.DateField()),
                ('is_potrjen', models.BooleanField(verbose_name='Potrjeno iz strani nadzornika', default=False)),
                ('zmin', models.IntegerField(verbose_name='zaokrožitev [min]', default=15)),
                ('element', models.ManyToManyField(blank=True, to='deli.ProjektnoMesto')),
                ('narocilo', models.ForeignKey(verbose_name='naročilo', to='narocila.Narocilo')),
                ('nosilec', models.ForeignKey(to='partnerji.Oseba')),
                ('planirano_opravilo', models.ForeignKey(null=True, blank=True, to='planiranje.PlaniranoOpravilo')),
                ('pomanjkljivost', models.ManyToManyField(blank=True, to='pomanjkljivosti.Pomanjkljivost')),
                ('zahtevek', models.ForeignKey(to='zahtevki.Zahtevek')),
            ],
            options={
                'verbose_name': 'Opravilo',
                'verbose_name_plural': 'Opravila',
            },
        ),
        migrations.CreateModel(
            name='VzorecOpravila',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('rok_izvedbe', models.DateField(null=True, blank=True)),
                ('is_potrjen', models.BooleanField(verbose_name='Potrjeno iz strani nadzornika', default=False)),
                ('element', models.ManyToManyField(to='deli.ProjektnoMesto')),
                ('narocilo', models.ForeignKey(verbose_name='naročilo', to='narocila.Narocilo')),
                ('nosilec', models.ForeignKey(to='partnerji.Oseba')),
                ('planirano_opravilo', models.ForeignKey(null=True, blank=True, to='planiranje.PlaniranoOpravilo')),
            ],
            options={
                'verbose_name': 'vzorec opravila',
                'verbose_name_plural': 'vzorci opravil',
            },
        ),
        migrations.AddField(
            model_name='delovrsta',
            name='skupina',
            field=models.ForeignKey(to='delovninalogi.DeloVrstaSklop'),
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
        migrations.AddField(
            model_name='delo',
            name='vrsta_dela',
            field=models.ForeignKey(null=True, blank=True, to='delovninalogi.DeloVrsta'),
        ),
    ]
