# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '__first__'),
        ('zahtevki', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sestanek',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_likvidiran', models.BooleanField(default=False)),
                ('status', models.IntegerField(choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano')], default=0)),
                ('oznaka', models.CharField(max_length=255, verbose_name='oznaka')),
                ('naziv', models.CharField(max_length=255, verbose_name='naziv')),
                ('opis', models.TextField(verbose_name='namen')),
                ('datum', models.DateField(verbose_name='datum sestanka')),
                ('prisotni', models.ManyToManyField(to='partnerji.Oseba', blank=True, verbose_name='prisotni')),
                ('sklicatelj', models.ForeignKey(to='partnerji.Partner', verbose_name='sklical')),
                ('zahtevek', models.ForeignKey(null=True, to='zahtevki.Zahtevek', blank=True, verbose_name='zahtevek')),
            ],
            options={
                'verbose_name_plural': 'sestanki',
                'verbose_name': 'sestanek',
            },
        ),
        migrations.CreateModel(
            name='Sklep',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_likvidiran', models.BooleanField(default=False)),
                ('zap_st', models.IntegerField(default=9999, verbose_name='zaporedna številka')),
                ('status', models.IntegerField(choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano')], default=0)),
                ('oznaka', models.CharField(max_length=255, verbose_name='oznaka')),
                ('opis', models.TextField(verbose_name='vsebina')),
                ('izvede', models.CharField(null=True, max_length=255, blank=True, verbose_name='izvede/realizira')),
                ('rok_izvedbe', models.DateField(null=True, blank=True, verbose_name='rok izvedbe')),
                ('rok_izvedbe_opis', models.CharField(null=True, max_length=255, blank=True, verbose_name='rok izvedbe opisno')),
                ('dopolnitev_sklepov', models.ManyToManyField(to='sestanki.Sklep', blank=True, related_name='_dopolnitev_sklepov_+', verbose_name='dopolnitev sklepov')),
            ],
            options={
                'verbose_name_plural': 'sklepi sestankov',
                'verbose_name': 'sklep sestanka',
            },
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_likvidiran', models.BooleanField(default=False)),
                ('zap_st', models.IntegerField(default=9999, verbose_name='zaporedna številka')),
                ('status', models.IntegerField(choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano')], default=0)),
                ('oznaka', models.CharField(max_length=255, verbose_name='oznaka')),
                ('naziv', models.CharField(max_length=255, verbose_name='naziv')),
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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_likvidiran', models.BooleanField(default=False)),
                ('zap_st', models.IntegerField(default=9999, verbose_name='zaporedna številka')),
                ('status', models.IntegerField(choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano')], default=0)),
                ('oznaka', models.CharField(max_length=255, verbose_name='oznaka')),
                ('naziv', models.CharField(max_length=255, verbose_name='naziv')),
                ('sestanek', models.ForeignKey(to='sestanki.Sestanek', verbose_name='sestanek')),
            ],
            options={
                'verbose_name_plural': 'dnevni red',
                'verbose_name': 'tocka dnevnega reda',
            },
        ),
        migrations.AddField(
            model_name='sklep',
            name='tocka',
            field=models.ForeignKey(to='sestanki.Tocka', verbose_name='točka sestanka'),
        ),
    ]
