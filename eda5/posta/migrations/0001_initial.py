# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import eda5.posta.models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aktivnost',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('datum_aktivnosti', models.DateField()),
                ('izvajalec', models.ForeignKey(related_name='izvajalec', verbose_name='izvajalec poštne storitve', to='partnerji.Oseba')),
            ],
            options={
                'verbose_name_plural': 'aktivnosti',
                'verbose_name': 'aktivnost',
            },
        ),
        migrations.CreateModel(
            name='Dokument',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('oznaka_baza', models.IntegerField(null=True, blank=True)),
                ('oznaka', models.CharField(max_length=50, verbose_name='številka dokumenta')),
                ('naziv', models.CharField(max_length=255, verbose_name='naziv')),
                ('datum_dokumenta', models.DateField()),
                ('kraj_izdaje', models.CharField(max_length=100, blank=True)),
                ('priponka', models.FileField(upload_to=eda5.posta.models.Dokument.dokument_directory_path)),
                ('aktivnost', models.OneToOneField(to='posta.Aktivnost')),
                ('avtor', models.ForeignKey(related_name='avtor', to='partnerji.Partner')),
                ('naslovnik', models.ForeignKey(related_name='naslovnik', to='partnerji.Partner')),
            ],
            options={
                'verbose_name_plural': 'dokumenti',
                'verbose_name': 'dokument',
            },
        ),
        migrations.CreateModel(
            name='SkupinaDokumenta',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('zap_st', models.IntegerField(verbose_name='zaporedna številka', default=9999)),
                ('oznaka', models.CharField(max_length=3, verbose_name='oznaka', unique=True)),
                ('naziv', models.CharField(max_length=255, verbose_name='naziv')),
            ],
            options={
                'verbose_name_plural': 'Skupine Dokumentov',
                'ordering': ('zap_st',),
                'verbose_name': 'Skupina Dokumentov',
            },
        ),
        migrations.CreateModel(
            name='VrstaDokumenta',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('zap_st', models.IntegerField(verbose_name='zaporedna številka', default=9999)),
                ('oznaka', models.CharField(max_length=3, verbose_name='oznaka', unique=True)),
                ('naziv', models.CharField(max_length=255, verbose_name='naziv')),
                ('skupina', models.ForeignKey(verbose_name='Skupina Dokumentov', to='posta.SkupinaDokumenta')),
            ],
            options={
                'verbose_name_plural': 'Vrste Dokumentov',
                'ordering': ('oznaka',),
                'verbose_name': 'Vrsta Dokumenta',
            },
        ),
        migrations.AddField(
            model_name='dokument',
            name='vrsta_dokumenta',
            field=models.ForeignKey(verbose_name='vrsta dokumenta', to='posta.VrstaDokumenta'),
        ),
        migrations.AlterUniqueTogether(
            name='dokument',
            unique_together=set([('oznaka', 'avtor', 'vrsta_dokumenta', 'datum_dokumenta')]),
        ),
    ]
