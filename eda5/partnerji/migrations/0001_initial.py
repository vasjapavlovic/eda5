# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banka',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('oznaka', models.CharField(max_length=50)),
                ('naziv', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Oseba',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('priimek', models.CharField(max_length=50)),
                ('ime', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('A', 'pooblaščenec'), ('B', 'delavec')], max_length=1)),
                ('kvalifikacije', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('oznaka', models.CharField(max_length=15)),
                ('dolgo_ime', models.CharField(max_length=255)),
                ('kratko_ime', models.CharField(max_length=100, blank=True)),
                ('naslov', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Posta',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('postna_stevilka', models.CharField(verbose_name='poštna številka', max_length=10)),
                ('naziv', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TRRacun',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('trr', models.CharField(verbose_name='stevilka računa', max_length=20)),
                ('banka', models.ForeignKey(to='partnerji.Banka')),
                ('partner', models.ForeignKey(verbose_name='partner', to='partnerji.Partner')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='partner',
            name='posta',
            field=models.ForeignKey(verbose_name='pošta', to='partnerji.Posta'),
        ),
        migrations.AddField(
            model_name='oseba',
            name='podjetje',
            field=models.ForeignKey(to='partnerji.Partner'),
        ),
    ]
