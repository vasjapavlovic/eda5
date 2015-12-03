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
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('id_1', models.IntegerField(serialize=False, primary_key=True)),
                ('vrsta_aktivnosti', models.IntegerField(choices=[(1, 'prejeta posta'), (2, 'izdana pošta')])),
                ('datum', models.DateField()),
                ('izvajalec', models.ForeignKey(to='partnerji.Oseba', verbose_name='izvajalec poštne storitve', related_name='izvajalec')),
                ('likvidiral', models.ForeignKey(to='partnerji.Oseba', verbose_name='pošto bo likvidiral', related_name='likvidiral')),
            ],
            options={
                'verbose_name': 'aktivnost',
                'verbose_name_plural': 'aktivnosti',
            },
        ),
        migrations.CreateModel(
            name='Dokument',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('oznaka', models.CharField(verbose_name='številka dokumenta', max_length=20)),
                ('naziv', models.CharField(verbose_name='naziv', max_length=255)),
                ('datum', models.DateField()),
                ('priponka', models.FileField(upload_to=eda5.posta.models.Dokument.dokument_directory_path, null=True, blank=True)),
                ('aktivnost', models.OneToOneField(to='posta.Aktivnost')),
                ('avtor', models.ForeignKey(to='partnerji.SkupinaPartnerjev', related_name='avtor')),
                ('naslovnik', models.ForeignKey(to='partnerji.SkupinaPartnerjev', related_name='naslovnik')),
            ],
            options={
                'verbose_name': 'dokument',
                'verbose_name_plural': 'dokumenti',
            },
        ),
        migrations.CreateModel(
            name='SkupinaDokumenta',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('oznaka', models.CharField(verbose_name='oznaka', max_length=3)),
                ('naziv', models.CharField(verbose_name='naziv', max_length=255)),
            ],
            options={
                'verbose_name': 'Skupina Dokumentov',
                'verbose_name_plural': 'Skupine Dokumentov',
            },
        ),
        migrations.CreateModel(
            name='VrstaDokumenta',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('oznaka', models.CharField(verbose_name='oznaka', max_length=3)),
                ('naziv', models.CharField(verbose_name='naziv', max_length=255)),
                ('zap_st', models.IntegerField(verbose_name='zaporedna številka')),
                ('skupina', models.ForeignKey(to='posta.SkupinaDokumenta', verbose_name='Skupina Dokumentov')),
            ],
            options={
                'verbose_name': 'Vrsta Dokumenta',
                'verbose_name_plural': 'Vrste Dokumentov',
            },
        ),
        migrations.AddField(
            model_name='dokument',
            name='vrsta_dokumenta',
            field=models.ForeignKey(to='posta.VrstaDokumenta', verbose_name='vrsta dokumenta'),
        ),
    ]
