# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0001_initial'),
        ('zahtevki', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpombaVnosa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('oznaka', models.CharField(verbose_name='oznaka', max_length=255)),
                ('opis', models.TextField(verbose_name='vsebina')),
                ('opomnil', models.CharField(verbose_name='opomnil', max_length=255, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'opomba vnosa',
                'verbose_name_plural': 'opombe vnosov',
            },
        ),
        migrations.CreateModel(
            name='Sestanek',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_likvidiran', models.BooleanField(default=False)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('oznaka', models.CharField(verbose_name='oznaka', max_length=255)),
                ('naziv', models.CharField(verbose_name='naziv', max_length=255)),
                ('opis', models.TextField(verbose_name='namen')),
                ('datum', models.DateField(verbose_name='datum sestanka')),
                ('prisotni', models.ManyToManyField(verbose_name='prisotni', to='partnerji.Oseba', blank=True)),
                ('sklicatelj', models.ForeignKey(verbose_name='sklical', to='partnerji.Partner')),
                ('zahtevek', models.ForeignKey(null=True, blank=True, verbose_name='zahtevek', to='zahtevki.Zahtevek')),
            ],
            options={
                'verbose_name': 'sestanek',
                'ordering': ['-datum'],
                'verbose_name_plural': 'sestanki',
            },
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_likvidiran', models.BooleanField(default=False)),
                ('zap_st', models.IntegerField(verbose_name='zaporedna številka', default=9999)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('oznaka', models.CharField(verbose_name='oznaka', max_length=255)),
                ('naziv', models.CharField(verbose_name='naziv', max_length=255)),
                ('opis', models.TextField(verbose_name='opis')),
            ],
            options={
                'verbose_name': 'tema',
                'verbose_name_plural': 'teme',
            },
        ),
        migrations.CreateModel(
            name='Tocka',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_likvidiran', models.BooleanField(default=False)),
                ('zap_st', models.IntegerField(verbose_name='zaporedna številka', default=9999)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('oznaka', models.CharField(verbose_name='oznaka', max_length=255)),
                ('naziv', models.CharField(verbose_name='naziv', max_length=255)),
                ('sestanek', models.ForeignKey(verbose_name='sestanek', to='sestanki.Sestanek')),
            ],
            options={
                'verbose_name': 'tocka dnevnega reda',
                'verbose_name_plural': 'dnevni red',
            },
        ),
        migrations.CreateModel(
            name='Vnos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_likvidiran', models.BooleanField(default=False)),
                ('zap_st', models.IntegerField(verbose_name='zaporedna številka', default=9999)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('oznaka', models.CharField(verbose_name='oznaka', max_length=255)),
                ('opis', models.TextField(verbose_name='vsebina')),
                ('izvede', models.CharField(verbose_name='izvede/realizira', max_length=255, null=True, blank=True)),
                ('rok_izvedbe', models.DateField(verbose_name='rok izvedbe', null=True, blank=True)),
                ('rok_izvedbe_opis', models.CharField(verbose_name='rok izvedbe opisno', max_length=255, null=True, blank=True)),
                ('dopolnitev_vnosov', models.ManyToManyField(verbose_name='dopolnitev vnosov', to='sestanki.Vnos', blank=True, related_name='_dopolnitev_vnosov_+')),
                ('tocka', models.ForeignKey(verbose_name='točka sestanka', to='sestanki.Tocka')),
            ],
            options={
                'verbose_name': 'vnos sestanka',
                'verbose_name_plural': 'vnosi sestankov',
            },
        ),
        migrations.CreateModel(
            name='Zadeva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_likvidiran', models.BooleanField(default=False)),
                ('zap_st', models.IntegerField(verbose_name='zaporedna številka', default=9999)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('oznaka', models.CharField(verbose_name='oznaka', max_length=255)),
                ('naziv', models.CharField(verbose_name='naziv', max_length=255)),
                ('opis', models.TextField(verbose_name='opis')),
                ('tema', models.ForeignKey(null=True, blank=True, verbose_name='tema', to='sestanki.Tema')),
            ],
            options={
                'verbose_name': 'zadeva',
                'verbose_name_plural': 'zadeve',
            },
        ),
        migrations.AddField(
            model_name='vnos',
            name='zadeva',
            field=models.ForeignKey(null=True, blank=True, verbose_name='zadeva', to='sestanki.Zadeva'),
        ),
        migrations.AddField(
            model_name='opombavnosa',
            name='vnos',
            field=models.ForeignKey(verbose_name='vnos sestanka', to='sestanki.Vnos'),
        ),
    ]
