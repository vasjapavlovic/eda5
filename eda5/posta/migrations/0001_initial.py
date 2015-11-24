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
            name='Aktivnost',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('id_1', models.IntegerField(primary_key=True, serialize=False)),
                ('vrsta_aktivnosti', models.IntegerField(choices=[(1, 'prejeta posta'), (2, 'izdana pošta')])),
                ('datum', models.DateField()),
                ('izvajalec', models.ForeignKey(related_name='izvajalec', verbose_name='izvajalec poštne storitve', to='partnerji.Oseba')),
                ('likvidiral', models.ForeignKey(related_name='likvidiral', verbose_name='pošto bo likvidiral', to='partnerji.Oseba')),
            ],
            options={
                'verbose_name': 'aktivnost',
                'verbose_name_plural': 'aktivnosti',
            },
        ),
        migrations.CreateModel(
            name='Dokument',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('oznaka', models.CharField(max_length=20, verbose_name='številka dokumenta')),
                ('naziv', models.CharField(max_length=255, verbose_name='naziv')),
                ('datum', models.DateField()),
                ('priponka', models.FileField(upload_to=eda5.posta.models.Dokument.dokument_directory_path, blank=True, null=True)),
                ('aktivnost', models.OneToOneField(to='posta.Aktivnost')),
                ('avtor', models.ForeignKey(related_name='avtor', to='partnerji.SkupinaPartnerjev')),
                ('naslovnik', models.ForeignKey(related_name='naslovnik', to='partnerji.SkupinaPartnerjev')),
            ],
            options={
                'verbose_name': 'dokument',
                'verbose_name_plural': 'dokumenti',
            },
        ),
        migrations.CreateModel(
            name='SkupinaDokumenta',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
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
