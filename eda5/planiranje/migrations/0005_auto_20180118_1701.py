# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0004_delstavbe_stavba'),
        ('planiranje', '0004_planiranoopravilo_osnova'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanAktivnost',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('oznaka', models.CharField(max_length=100, blank=True, null=True)),
                ('oznaka_gen', models.CharField(max_length=100, blank=True, null=True)),
                ('naziv', models.CharField(max_length=255, blank=True, null=True)),
                ('opis', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('perioda_enota', models.CharField(max_length=5, choices=[('dan', 'Dan'), ('teden', 'Teden'), ('mesec', 'Mesec'), ('leto', 'Leto')], verbose_name='Perioda ENOTA')),
                ('perioda_enota_kolicina', models.IntegerField(verbose_name='Perioda KRATNIK ENOTE')),
                ('perioda_kolicina_na_enoto', models.IntegerField(verbose_name='Perioda KOLIČINA NA ENOTO')),
                ('plan', models.ForeignKey(verbose_name='plan', to='planiranje.Plan')),
            ],
            options={
                'ordering': ('oznaka',),
                'verbose_name_plural': 'Planirane Aktivnosti',
                'verbose_name': 'Planirana Aktivnost',
            },
        ),
        migrations.CreateModel(
            name='PlanKontrolaSkupina',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('oznaka', models.CharField(max_length=100, blank=True, null=True)),
                ('oznaka_gen', models.CharField(max_length=100, blank=True, null=True)),
                ('naziv', models.CharField(max_length=255, blank=True, null=True)),
                ('opis', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('plan_aktivnost', models.ForeignKey(verbose_name='planirana aktivnost', to='planiranje.PlanAktivnost')),
            ],
            options={
                'ordering': ['oznaka'],
                'verbose_name': 'Skupina planiranih kontrol',
            },
        ),
        migrations.CreateModel(
            name='PlanKontrolaSpecifikacija',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('oznaka', models.CharField(max_length=100, blank=True, null=True)),
                ('oznaka_gen', models.CharField(max_length=100, blank=True, null=True)),
                ('naziv', models.CharField(max_length=255, blank=True, null=True)),
                ('opis', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('vrednost_vrsta', models.IntegerField(default=1, choices=[(1, 'check'), (2, 'text'), (3, 'select')], verbose_name='vrsta vrednosti')),
                ('plan_kontrola_skupina', models.ForeignKey(to='planiranje.PlanKontrolaSkupina', blank=True, verbose_name='skupina planiranih kontrol', null=True)),
            ],
            options={
                'ordering': ['oznaka'],
            },
        ),
        migrations.CreateModel(
            name='PlanKontrolaSpecifikacijaOpcijaSelect',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('oznaka', models.CharField(max_length=100, blank=True, null=True)),
                ('oznaka_gen', models.CharField(max_length=100, blank=True, null=True)),
                ('naziv', models.CharField(max_length=255, blank=True, null=True)),
                ('opis', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('plan_kontrola_specifikacija', models.ForeignKey(verbose_name='specifikacija planirane kontrole', to='planiranje.PlanKontrolaSpecifikacija')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='planiranoopravilo',
            name='plan',
            field=models.ForeignKey(verbose_name='plan', to='planiranje.Plan'),
        ),
        migrations.AddField(
            model_name='planaktivnost',
            name='planirano_opravilo',
            field=models.ForeignKey(to='planiranje.PlaniranoOpravilo', blank=True, verbose_name='planirano opravilo', null=True),
        ),
        migrations.AddField(
            model_name='planaktivnost',
            name='projektno_mesto',
            field=models.ManyToManyField(blank=True, verbose_name='projektno mesto', to='deli.ProjektnoMesto'),
        ),
    ]
