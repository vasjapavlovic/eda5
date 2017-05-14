# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('narocila', '__first__'),
        ('racunovodstvo', '__first__'),
        ('partnerji', '__first__'),
        ('zahtevki', '__first__'),
        ('pomanjkljivosti', '__first__'),
        ('planiranje', '__first__'),
        ('naloge', '0001_initial'),
        ('deli', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano')])),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('datum', models.DateField(blank=True, null=True)),
                ('time_start', models.DurationField(blank=True, verbose_name='Ura:Začeto', null=True)),
                ('time_stop', models.DurationField(blank=True, verbose_name='Ura:Končano', null=True)),
                ('delo_cas_rac', models.DecimalField(blank=True, max_digits=5, verbose_name='Porabljen čas [UR]', null=True, decimal_places=2)),
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
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano')])),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('datum_plan', models.DateField(blank=True, verbose_name='V planu za dne', null=True)),
                ('datum_start', models.DateField(blank=True, verbose_name='Začeto dne', null=True)),
                ('datum_stop', models.DateField(blank=True, verbose_name='Končano dne', null=True)),
                ('nosilec', models.ForeignKey(blank=True, verbose_name='Izvajalec (kdo bo delo izvedel)', null=True, to='partnerji.Oseba')),
            ],
            options={
                'verbose_name_plural': 'Delovni Nalogi',
                'verbose_name': 'Delovni Nalog',
            },
        ),
        migrations.CreateModel(
            name='DeloVrsta',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('oznaka', models.CharField(unique=True, max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('zap_st', models.IntegerField(default=99)),
                ('cena', models.DecimalField(max_digits=4, decimal_places=2)),
                ('stopnja_ddv', models.DecimalField(max_digits=4, decimal_places=3)),
            ],
            options={
                'verbose_name_plural': 'vrste del',
                'verbose_name': 'vrsta dela',
            },
        ),
        migrations.CreateModel(
            name='DeloVrstaSklop',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('oznaka', models.CharField(unique=True, max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('zap_st', models.IntegerField(default=99)),
            ],
            options={
                'verbose_name_plural': 'sklopi vrst del',
                'verbose_name': 'sklop vrst del',
            },
        ),
        migrations.CreateModel(
            name='Opravilo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano')])),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('rok_izvedbe', models.DateField()),
                ('is_potrjen', models.BooleanField(verbose_name='Potrjeno iz strani nadzornika', default=False)),
                ('zmin', models.IntegerField(verbose_name='zaokrožitev [min]', default=15)),
                ('element', models.ManyToManyField(blank=True, to='deli.ProjektnoMesto')),
                ('naloga', models.ManyToManyField(blank=True, to='naloge.Naloga')),
                ('narocilo', models.ForeignKey(to='narocila.Narocilo', verbose_name='naročilo')),
                ('nosilec', models.ForeignKey(to='partnerji.Oseba')),
                ('planirano_opravilo', models.ForeignKey(blank=True, to='planiranje.PlaniranoOpravilo', null=True)),
                ('pomanjkljivost', models.ManyToManyField(blank=True, to='pomanjkljivosti.Pomanjkljivost')),
                ('vrsta_stroska', models.ForeignKey(blank=True, verbose_name='vrsta stroška', null=True, to='racunovodstvo.VrstaStroska')),
                ('zahtevek', models.ForeignKey(to='zahtevki.Zahtevek')),
            ],
            options={
                'verbose_name_plural': 'Opravila',
                'verbose_name': 'Opravilo',
            },
        ),
        migrations.CreateModel(
            name='VzorecOpravila',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('rok_izvedbe', models.DateField(blank=True, null=True)),
                ('is_potrjen', models.BooleanField(verbose_name='Potrjeno iz strani nadzornika', default=False)),
                ('element', models.ManyToManyField(to='deli.ProjektnoMesto')),
                ('narocilo', models.ForeignKey(to='narocila.Narocilo', verbose_name='naročilo')),
                ('nosilec', models.ForeignKey(to='partnerji.Oseba')),
                ('planirano_opravilo', models.ForeignKey(blank=True, to='planiranje.PlaniranoOpravilo', null=True)),
            ],
            options={
                'verbose_name_plural': 'vzorci opravil',
                'verbose_name': 'vzorec opravila',
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
            field=models.ForeignKey(to='delovninalogi.DelovniNalog', verbose_name='delovni nalog'),
        ),
        migrations.AddField(
            model_name='delo',
            name='vrsta_dela',
            field=models.ForeignKey(blank=True, to='delovninalogi.DeloVrsta', null=True),
        ),
    ]
