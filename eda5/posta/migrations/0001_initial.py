# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import eda5.posta.models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dokument',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_likvidiran', models.BooleanField(default=False)),
                ('oznaka', models.CharField(max_length=20, verbose_name='številka dokumenta')),
                ('datum', models.DateField()),
                ('opis', models.CharField(max_length=255, verbose_name='opis')),
                ('priponka', models.FileField(upload_to=eda5.posta.models.Dokument.dokument_directory_path)),
                ('naslovnik', models.ForeignKey(related_name='naslovnik', verbose_name='naslovnik', to='partnerji.SkupinaPartnerjev')),
                ('posiljatelj', models.ForeignKey(related_name='posiljatelj', verbose_name='pošiljatelj', to='partnerji.SkupinaPartnerjev')),
            ],
            options={
                'verbose_name': 'dokument',
                'verbose_name_plural': 'dokumenti',
            },
        ),
        migrations.CreateModel(
            name='PostnaStoritev',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('aktivnost', models.IntegerField(choices=[(1, 'prejeta posta'), (2, 'izdana pošta')])),
                ('datum', models.DateField()),
                ('dokument', models.OneToOneField(to='posta.Dokument')),
                ('izvajalec', models.ForeignKey(verbose_name='izvajalec poštne storitve', to='partnerji.Oseba')),
            ],
            options={
                'verbose_name': 'poštna storitev',
                'verbose_name_plural': 'poštne storitve',
            },
        ),
        migrations.CreateModel(
            name='SkupinaDokumenta',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('oznaka', models.CharField(max_length=3, verbose_name='oznaka')),
                ('naziv', models.CharField(max_length=255, verbose_name='naziv')),
            ],
            options={
                'verbose_name': 'Skupina Dokumentov',
                'verbose_name_plural': 'Skupine Dokumentov',
            },
        ),
        migrations.CreateModel(
            name='VrstaDokumenta',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('oznaka', models.CharField(max_length=3, verbose_name='oznaka')),
                ('naziv', models.CharField(max_length=255, verbose_name='naziv')),
                ('zap_st', models.IntegerField(verbose_name='zaporedna številka')),
                ('skupina', models.ForeignKey(verbose_name='Skupina Dokumentov', to='posta.SkupinaDokumenta')),
            ],
            options={
                'verbose_name': 'Vrsta Dokumenta',
                'verbose_name_plural': 'Vrste Dokumentov',
            },
        ),
        migrations.AddField(
            model_name='dokument',
            name='vrsta_dokumenta',
            field=models.ForeignKey(verbose_name='vrsta dokumenta', to='posta.VrstaDokumenta'),
        ),
    ]
