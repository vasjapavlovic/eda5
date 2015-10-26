# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0011_auto_20151025_1701'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dokument',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('datum_prejema', models.DateField(verbose_name='datum prejema')),
                ('oznaka', models.CharField(max_length=20, verbose_name='številka dokumenta')),
                ('opis', models.CharField(max_length=255, verbose_name='naziv')),
                ('priponka', models.FileField(upload_to='prejeta_posta/')),
                ('posiljatelj', models.ForeignKey(to='partnerji.Partner', verbose_name='avtor dokumenta')),
            ],
            options={
                'verbose_name_plural': 'Dokumenti',
                'verbose_name': 'Dokument',
            },
        ),
        migrations.CreateModel(
            name='SkupinaDokumenta',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
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
