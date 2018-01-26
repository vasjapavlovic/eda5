# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delovninalogi', '0001_initial'),
        ('planiranje', '0001_initial'),
        ('deli', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aktivnost',
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
                ('opravilo', models.ForeignKey(verbose_name='opravilo', to='delovninalogi.Opravilo')),
                ('plan_aktivnost', models.ForeignKey(null=True, blank=True, to='planiranje.PlanAktivnost')),
            ],
            options={
                'verbose_name_plural': 'Aktivnosti',
                'verbose_name': 'Aktivnost',
                'ordering': ('oznaka',),
            },
        ),
        migrations.CreateModel(
            name='KontrolaSkupina',
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
                ('aktivnost', models.ForeignKey(verbose_name='aktivnost', to='kontrolnilist.Aktivnost')),
                ('plan_kontrola_skupina', models.ForeignKey(verbose_name='planiranja skupina kontrol', to='planiranje.PlanKontrolaSkupina')),
            ],
            options={
                'verbose_name': 'Skupina kontrol',
                'ordering': ['oznaka'],
            },
        ),
        migrations.CreateModel(
            name='KontrolaSpecifikacija',
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
                ('kontrola_skupina', models.ForeignKey(null=True, verbose_name='skupina kontrol', blank=True, to='kontrolnilist.KontrolaSkupina')),
                ('plan_kontrola_specifikacija', models.ForeignKey(null=True, verbose_name='planirana kontrola specifikacija', blank=True, to='planiranje.PlanKontrolaSpecifikacija')),
                ('projektno_mesto', models.ManyToManyField(blank=True, to='deli.ProjektnoMesto', verbose_name='projektno mesto')),
            ],
            options={
                'ordering': ['oznaka'],
            },
        ),
        migrations.CreateModel(
            name='KontrolaSpecifikacijaOpcijaSelect',
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
                ('kontrola_specifikacija', models.ForeignKey(verbose_name='specifikacija kontrole', to='kontrolnilist.KontrolaSpecifikacija')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='KontrolaVrednost',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('oznaka', models.CharField(blank=True, max_length=100, null=True)),
                ('oznaka_gen', models.CharField(blank=True, max_length=100, null=True)),
                ('naziv', models.CharField(blank=True, max_length=255, null=True)),
                ('opis', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('vrednost_check', models.BooleanField(default=False, verbose_name='vrednost check')),
                ('vrednost_yes_no', models.IntegerField(blank=True, verbose_name='vrednost DA/NE', null=True, choices=[(1, 'DA'), (-1, 'NE')])),
                ('vrednost_text', models.CharField(blank=True, max_length=255, null=True, verbose_name='vrednost text')),
                ('vrednost_number', models.DecimalField(max_length=255, null=True, verbose_name='vrednost število', blank=True, max_digits=50, decimal_places=2)),
                ('delovni_nalog', models.ForeignKey(verbose_name='delovni nalog', to='delovninalogi.DelovniNalog')),
                ('kontrola_specifikacija', models.ForeignKey(verbose_name='specifikacija kontrole', to='kontrolnilist.KontrolaSpecifikacija')),
                ('projektno_mesto', models.ForeignKey(verbose_name='projektno mesto', to='deli.ProjektnoMesto')),
                ('vrednost_select', models.ForeignKey(null=True, verbose_name='vrednost select', blank=True, to='kontrolnilist.KontrolaSpecifikacijaOpcijaSelect')),
            ],
            options={
                'verbose_name_plural': 'vrednosti kontrol',
                'verbose_name': 'vrednost kontrole',
            },
        ),
    ]
