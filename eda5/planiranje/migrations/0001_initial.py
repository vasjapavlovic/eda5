# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0001_initial'),
        ('deli', '0001_initial'),
        ('predpisi', '0001_initial'),
        ('zahtevki', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('oznaka', models.CharField(max_length=25)),
                ('naziv', models.CharField(max_length=255)),
                ('zap_st', models.IntegerField(verbose_name='zaporedna številka', default=0)),
                ('opis', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'plani',
                'verbose_name': 'plan',
            },
        ),
        migrations.CreateModel(
            name='PlanAktivnost',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('oznaka', models.CharField(blank=True, max_length=100, null=True)),
                ('oznaka_gen', models.CharField(blank=True, max_length=100, null=True)),
                ('naziv', models.CharField(blank=True, max_length=255, null=True)),
                ('opis', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('zap_st', models.IntegerField(verbose_name='zaporedna številka', default=9999)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('perioda_enota', models.CharField(verbose_name='Perioda ENOTA', max_length=5, choices=[('dan', 'Dan'), ('teden', 'Teden'), ('mesec', 'Mesec'), ('leto', 'Leto')])),
                ('perioda_enota_kolicina', models.IntegerField(verbose_name='Perioda KRATNIK ENOTE')),
                ('perioda_kolicina_na_enoto', models.IntegerField(verbose_name='Perioda KOLIČINA NA ENOTO')),
                ('plan', models.ForeignKey(verbose_name='plan', to='planiranje.Plan')),
            ],
            options={
                'verbose_name_plural': 'Planirane Aktivnosti',
                'verbose_name': 'Planirana Aktivnost',
                'ordering': ('oznaka',),
            },
        ),
        migrations.CreateModel(
            name='PlaniranaAktivnost',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('naziv_opravila_izven_plana', models.CharField(blank=True, max_length=255)),
                ('artikel_plan', models.ForeignKey(null=True, blank=True, to='katalog.ArtikelPlan')),
                ('element', models.ForeignKey(null=True, blank=True, to='deli.Element')),
            ],
            options={
                'verbose_name_plural': 'planirane aktivnosti',
                'verbose_name': 'planirana aktivnost',
            },
        ),
        migrations.CreateModel(
            name='PlaniranoOpravilo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('oznaka', models.CharField(max_length=25)),
                ('naziv', models.CharField(max_length=255)),
                ('namen', models.CharField(max_length=255)),
                ('obseg', models.TextField()),
                ('perioda_predpisana_enota', models.CharField(verbose_name='enota periode', max_length=5, choices=[('dan', 'Dan'), ('teden', 'Teden'), ('mesec', 'Mesec'), ('leto', 'Leto')])),
                ('perioda_predpisana_enota_kolicina', models.IntegerField(verbose_name='kolicina enote periode')),
                ('perioda_predpisana_kolicina_na_enoto', models.IntegerField(verbose_name='kolicina na enoto periode')),
                ('datum_prve_izvedbe', models.DateField(blank=True, null=True)),
                ('datum_izvedeno_dne', models.DateField(blank=True, null=True, verbose_name='Izvedeno dne')),
                ('datum_naslednjega_opravila', models.DateField(blank=True, null=True, verbose_name='Naslednji pregled')),
                ('zmin', models.IntegerField(verbose_name='zaokrožitev [min]', default=15)),
                ('opomba', models.TextField(blank=True)),
                ('osnova', models.ForeignKey(null=True, blank=True, to='predpisi.PredpisSklop')),
                ('plan', models.ForeignKey(verbose_name='plan', to='planiranje.Plan')),
            ],
            options={
                'verbose_name_plural': 'planirana opravila',
                'verbose_name': 'planirano opravilo',
                'ordering': ('oznaka',),
            },
        ),
        migrations.CreateModel(
            name='PlanKontrolaSkupina',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('oznaka', models.CharField(blank=True, max_length=100, null=True)),
                ('oznaka_gen', models.CharField(blank=True, max_length=100, null=True)),
                ('naziv', models.CharField(blank=True, max_length=255, null=True)),
                ('opis', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('zap_st', models.IntegerField(verbose_name='zaporedna številka', default=9999)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('plan_aktivnost', models.ForeignKey(verbose_name='planirana aktivnost', to='planiranje.PlanAktivnost')),
            ],
            options={
                'verbose_name': 'Skupina planiranih kontrol',
                'ordering': ['oznaka'],
            },
        ),
        migrations.CreateModel(
            name='PlanKontrolaSpecifikacija',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('oznaka', models.CharField(blank=True, max_length=100, null=True)),
                ('oznaka_gen', models.CharField(blank=True, max_length=100, null=True)),
                ('naziv', models.CharField(blank=True, max_length=255, null=True)),
                ('opis', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('zap_st', models.IntegerField(verbose_name='zaporedna številka', default=9999)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('vrednost_vrsta', models.IntegerField(verbose_name='vrsta vrednosti', default=1, choices=[(1, 'check'), (2, 'text'), (4, 'number'), (5, 'yes_no'), (3, 'select')])),
                ('plan_kontrola_skupina', models.ForeignKey(null=True, verbose_name='skupina planiranih kontrol', blank=True, to='planiranje.PlanKontrolaSkupina')),
                ('projektno_mesto', models.ManyToManyField(blank=True, to='deli.ProjektnoMesto', verbose_name='projektno mesto')),
            ],
            options={
                'ordering': ['oznaka'],
            },
        ),
        migrations.CreateModel(
            name='PlanKontrolaSpecifikacijaOpcijaSelect',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('oznaka', models.CharField(blank=True, max_length=100, null=True)),
                ('oznaka_gen', models.CharField(blank=True, max_length=100, null=True)),
                ('naziv', models.CharField(blank=True, max_length=255, null=True)),
                ('opis', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('zap_st', models.IntegerField(verbose_name='zaporedna številka', default=9999)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('plan_kontrola_specifikacija', models.ForeignKey(verbose_name='specifikacija planirane kontrole', to='planiranje.PlanKontrolaSpecifikacija')),
            ],
            options={
                'ordering': ['zap_st', 'oznaka'],
            },
        ),
        migrations.CreateModel(
            name='SkupinaPlanov',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=25)),
                ('naziv', models.CharField(max_length=255)),
                ('zap_st', models.IntegerField(verbose_name='zaporedna številka', default=0)),
            ],
            options={
                'verbose_name_plural': 'skupine planov',
                'verbose_name': 'skupina planov',
                'ordering': ('zap_st',),
            },
        ),
        migrations.AddField(
            model_name='planiranaaktivnost',
            name='planirano_opravilo',
            field=models.ForeignKey(null=True, blank=True, to='planiranje.PlaniranoOpravilo'),
        ),
        migrations.AddField(
            model_name='planaktivnost',
            name='planirano_opravilo',
            field=models.ForeignKey(null=True, verbose_name='planirano opravilo', blank=True, to='planiranje.PlaniranoOpravilo'),
        ),
        migrations.AddField(
            model_name='plan',
            name='sklop',
            field=models.ForeignKey(to='planiranje.SkupinaPlanov'),
        ),
        migrations.AddField(
            model_name='plan',
            name='zahtevek',
            field=models.ForeignKey(null=True, blank=True, to='zahtevki.Zahtevek'),
        ),
    ]
