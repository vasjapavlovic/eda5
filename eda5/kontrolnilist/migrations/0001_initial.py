# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delovninalogi', '0012_auto_20180106_1001'),
        ('deli', '0003_remove_projektnomesto_tip_elementa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aktivnost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('oznaka', models.CharField(null=True, blank=True, max_length=100)),
                ('oznaka_gen', models.CharField(null=True, blank=True, max_length=100)),
                ('naziv', models.CharField(null=True, blank=True, max_length=255)),
                ('opis', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('opravilo', models.ForeignKey(blank=True, to='delovninalogi.Opravilo', null=True, verbose_name='opravilo')),
                ('projektno_mesto', models.ManyToManyField(verbose_name='projektno mesto', to='deli.ProjektnoMesto', blank=True)),
            ],
            options={
                'ordering': ('oznaka',),
                'verbose_name': 'Aktivnost',
                'verbose_name_plural': 'Aktivnosti',
            },
        ),
        migrations.CreateModel(
            name='AktivnostParameterSpecifikacija',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('oznaka', models.CharField(null=True, blank=True, max_length=100)),
                ('oznaka_gen', models.CharField(null=True, blank=True, max_length=100)),
                ('naziv', models.CharField(null=True, blank=True, max_length=255)),
                ('opis', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('vrsta_vnosa', models.IntegerField(verbose_name='vrsta vnosa', default=1, choices=[(1, 'check'), (2, 'text'), (3, 'select')])),
                ('aktivnost', models.ForeignKey(verbose_name='aktivnost', to='kontrolnilist.Aktivnost')),
            ],
            options={
                'ordering': ['oznaka'],
            },
        ),
        migrations.CreateModel(
            name='OpcijaSelect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('oznaka', models.CharField(null=True, blank=True, max_length=100)),
                ('oznaka_gen', models.CharField(null=True, blank=True, max_length=100)),
                ('naziv', models.CharField(null=True, blank=True, max_length=255)),
                ('opis', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('aktivnost_parameter_specifikacija', models.ForeignKey(verbose_name='aktivnost parameter specifikacija', to='kontrolnilist.AktivnostParameterSpecifikacija')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
