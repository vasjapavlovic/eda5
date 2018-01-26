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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('oznaka_baza', models.IntegerField(blank=True, null=True)),
                ('oznaka', models.CharField(verbose_name='številka dokumenta', max_length=50)),
                ('naziv', models.CharField(verbose_name='naziv', max_length=255)),
                ('datum_dokumenta', models.DateField()),
                ('kraj_izdaje', models.CharField(blank=True, max_length=100)),
                ('priponka', models.FileField(upload_to=eda5.posta.models.Dokument.dokument_directory_path)),
                ('aktivnost', models.OneToOneField(to='posta.Aktivnost')),
                ('avtor', models.ForeignKey(to='partnerji.Partner', related_name='avtor')),
                ('naslovnik', models.ForeignKey(to='partnerji.Partner', related_name='naslovnik')),
            ],
            options={
                'verbose_name_plural': 'dokumenti',
                'verbose_name': 'dokument',
            },
        ),
        migrations.CreateModel(
            name='SkupinaDokumenta',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('zap_st', models.IntegerField(verbose_name='zaporedna številka', default=9999)),
                ('oznaka', models.CharField(verbose_name='oznaka', max_length=3, unique=True)),
                ('naziv', models.CharField(verbose_name='naziv', max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Skupine Dokumentov',
                'verbose_name': 'Skupina Dokumentov',
                'ordering': ('zap_st',),
            },
        ),
        migrations.CreateModel(
            name='VrstaDokumenta',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('zap_st', models.IntegerField(verbose_name='zaporedna številka', default=9999)),
                ('oznaka', models.CharField(verbose_name='oznaka', max_length=3, unique=True)),
                ('naziv', models.CharField(verbose_name='naziv', max_length=255)),
                ('skupina', models.ForeignKey(verbose_name='Skupina Dokumentov', to='posta.SkupinaDokumenta')),
            ],
            options={
                'verbose_name_plural': 'Vrste Dokumentov',
                'verbose_name': 'Vrsta Dokumenta',
                'ordering': ('oznaka',),
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
