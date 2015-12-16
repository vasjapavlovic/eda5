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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('vrsta_aktivnosti', models.IntegerField(choices=[(1, 'prejeta posta'), (2, 'izdana pošta')])),
                ('datum', models.DateField()),
                ('izvajalec', models.ForeignKey(to='partnerji.Oseba', verbose_name='izvajalec poštne storitve', related_name='izvajalec')),
                ('likvidiral', models.ForeignKey(to='partnerji.Oseba', verbose_name='pošto bo likvidiral', related_name='likvidiral')),
            ],
            options={
                'verbose_name_plural': 'aktivnosti',
                'verbose_name': 'aktivnost',
            },
        ),
        migrations.CreateModel(
            name='Dokument',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('oznaka', models.CharField(max_length=20, verbose_name='številka dokumenta')),
                ('naziv', models.CharField(max_length=255, verbose_name='naziv')),
                ('datum', models.DateField()),
                ('priponka', models.FileField(blank=True, upload_to=eda5.posta.models.Dokument.dokument_directory_path, null=True)),
                ('aktivnost', models.OneToOneField(to='posta.Aktivnost')),
                ('avtor', models.ForeignKey(to='partnerji.SkupinaPartnerjev', related_name='avtor')),
                ('naslovnik', models.ForeignKey(to='partnerji.SkupinaPartnerjev', related_name='naslovnik')),
            ],
            options={
                'verbose_name_plural': 'dokumenti',
                'verbose_name': 'dokument',
            },
        ),
        migrations.CreateModel(
            name='SkupinaDokumenta',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('oznaka', models.CharField(max_length=3, verbose_name='oznaka')),
                ('naziv', models.CharField(max_length=255, verbose_name='naziv')),
            ],
            options={
                'verbose_name_plural': 'Skupine Dokumentov',
                'verbose_name': 'Skupina Dokumentov',
            },
        ),
        migrations.CreateModel(
            name='VrstaDokumenta',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('oznaka', models.CharField(max_length=3, verbose_name='oznaka')),
                ('naziv', models.CharField(max_length=255, verbose_name='naziv')),
                ('zap_st', models.IntegerField(verbose_name='zaporedna številka')),
                ('skupina', models.ForeignKey(to='posta.SkupinaDokumenta', verbose_name='Skupina Dokumentov')),
            ],
            options={
                'verbose_name_plural': 'Vrste Dokumentov',
                'verbose_name': 'Vrsta Dokumenta',
            },
        ),
        migrations.AddField(
            model_name='dokument',
            name='vrsta_dokumenta',
            field=models.ForeignKey(to='posta.VrstaDokumenta', verbose_name='vrsta dokumenta'),
        ),
    ]
