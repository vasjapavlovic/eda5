# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '0001_initial'),
        ('partnerji', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpombaVnosa',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('oznaka', models.CharField(verbose_name='oznaka', max_length=255)),
                ('opis', models.TextField(verbose_name='vsebina')),
                ('opomnil', models.CharField(blank=True, max_length=255, null=True, verbose_name='opomnil')),
            ],
            options={
                'verbose_name_plural': 'opombe vnosov',
                'verbose_name': 'opomba vnosa',
            },
        ),
        migrations.CreateModel(
            name='Sestanek',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_likvidiran', models.BooleanField(default=False)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('oznaka', models.CharField(verbose_name='oznaka', max_length=255)),
                ('naziv', models.CharField(verbose_name='naziv', max_length=255)),
                ('opis', models.TextField(verbose_name='namen')),
                ('datum', models.DateField(verbose_name='datum sestanka')),
                ('prisotni', models.ManyToManyField(blank=True, to='partnerji.Oseba', verbose_name='prisotni')),
                ('sklicatelj', models.ForeignKey(verbose_name='sklical', to='partnerji.Partner')),
                ('zahtevek', models.ForeignKey(null=True, verbose_name='zahtevek', blank=True, to='zahtevki.Zahtevek')),
            ],
            options={
                'verbose_name_plural': 'sestanki',
                'verbose_name': 'sestanek',
                'ordering': ['-datum'],
            },
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_likvidiran', models.BooleanField(default=False)),
                ('zap_st', models.IntegerField(verbose_name='zaporedna številka', default=9999)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('oznaka', models.CharField(verbose_name='oznaka', max_length=255)),
                ('naziv', models.CharField(verbose_name='naziv', max_length=255)),
                ('opis', models.TextField(verbose_name='opis')),
            ],
            options={
                'verbose_name_plural': 'teme',
                'verbose_name': 'tema',
            },
        ),
        migrations.CreateModel(
            name='Tocka',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_likvidiran', models.BooleanField(default=False)),
                ('zap_st', models.IntegerField(verbose_name='zaporedna številka', default=9999)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('oznaka', models.CharField(verbose_name='oznaka', max_length=255)),
                ('naziv', models.CharField(verbose_name='naziv', max_length=255)),
                ('sestanek', models.ForeignKey(verbose_name='sestanek', to='sestanki.Sestanek')),
            ],
            options={
                'verbose_name_plural': 'dnevni red',
                'verbose_name': 'tocka dnevnega reda',
            },
        ),
        migrations.CreateModel(
            name='Vnos',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_likvidiran', models.BooleanField(default=False)),
                ('zap_st', models.IntegerField(verbose_name='zaporedna številka', default=9999)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('oznaka', models.CharField(verbose_name='oznaka', max_length=255)),
                ('opis', models.TextField(verbose_name='vsebina')),
                ('izvede', models.CharField(blank=True, max_length=255, null=True, verbose_name='izvede/realizira')),
                ('rok_izvedbe', models.DateField(blank=True, null=True, verbose_name='rok izvedbe')),
                ('rok_izvedbe_opis', models.CharField(blank=True, max_length=255, null=True, verbose_name='rok izvedbe opisno')),
                ('dopolnitev_vnosov', models.ManyToManyField(blank=True, to='sestanki.Vnos', related_name='_dopolnitev_vnosov_+', verbose_name='dopolnitev vnosov')),
                ('tocka', models.ForeignKey(verbose_name='točka sestanka', to='sestanki.Tocka')),
            ],
            options={
                'verbose_name_plural': 'vnosi sestankov',
                'verbose_name': 'vnos sestanka',
            },
        ),
        migrations.CreateModel(
            name='Zadeva',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_likvidiran', models.BooleanField(default=False)),
                ('zap_st', models.IntegerField(verbose_name='zaporedna številka', default=9999)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('oznaka', models.CharField(verbose_name='oznaka', max_length=255)),
                ('naziv', models.CharField(verbose_name='naziv', max_length=255)),
                ('opis', models.TextField(verbose_name='opis')),
                ('tema', models.ForeignKey(null=True, verbose_name='tema', blank=True, to='sestanki.Tema')),
            ],
            options={
                'verbose_name_plural': 'zadeve',
                'verbose_name': 'zadeva',
            },
        ),
        migrations.AddField(
            model_name='vnos',
            name='zadeva',
            field=models.ForeignKey(null=True, verbose_name='zadeva', blank=True, to='sestanki.Zadeva'),
        ),
        migrations.AddField(
            model_name='opombavnosa',
            name='vnos',
            field=models.ForeignKey(verbose_name='vnos sestanka', to='sestanki.Vnos'),
        ),
    ]
