# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0001_initial'),
        ('partnerji', '0001_initial'),
        ('delovninalogi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artikel',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('oznaka', models.CharField(max_length=50)),
                ('naziv', models.CharField(max_length=255)),
                ('opis', models.CharField(blank=True, max_length=255)),
                ('st_police', models.IntegerField(blank=True, null=True, verbose_name='številka police')),
            ],
            options={
                'verbose_name_plural': 'artikli',
                'verbose_name': 'artikel',
            },
        ),
        migrations.CreateModel(
            name='Dnevnik',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('kom', models.IntegerField()),
                ('cena', models.DecimalField(blank=True, max_digits=6, null=True, decimal_places=2)),
                ('stopnja_ddv', models.DecimalField(blank=True, max_digits=4, null=True, decimal_places=3)),
                ('artikel', models.ForeignKey(to='skladisce.Artikel')),
                ('delovninalog', models.ForeignKey(null=True, verbose_name='delovni nalog', blank=True, to='delovninalogi.DelovniNalog')),
            ],
            options={
                'verbose_name_plural': 'dnevnik',
                'verbose_name': 'dnevnik',
            },
        ),
        migrations.CreateModel(
            name='Dobava',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('datum', models.DateField(verbose_name='datum prevzema blaga')),
                ('dobavitelj', models.ForeignKey(to='partnerji.Partner')),
                ('dobavnica', models.OneToOneField(to='posta.Dokument')),
                ('prevzel', models.ForeignKey(to='partnerji.Oseba')),
            ],
            options={
                'verbose_name_plural': 'dobave',
                'verbose_name': 'dobava',
            },
        ),
        migrations.CreateModel(
            name='SklopArtikla',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=50)),
                ('naziv', models.CharField(max_length=255)),
                ('opis', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name_plural': 'sklopi artiklov',
                'verbose_name': 'sklop artikla',
            },
        ),
        migrations.CreateModel(
            name='TipArtikla',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=50)),
                ('naziv', models.CharField(max_length=255)),
                ('opis', models.CharField(blank=True, max_length=255)),
                ('sklop', models.ForeignKey(to='skladisce.SklopArtikla')),
            ],
            options={
                'verbose_name_plural': 'tipi artiklov',
                'verbose_name': 'tip artikla',
            },
        ),
        migrations.AddField(
            model_name='dnevnik',
            name='dobava',
            field=models.ForeignKey(null=True, blank=True, to='skladisce.Dobava'),
        ),
        migrations.AddField(
            model_name='dnevnik',
            name='likvidiral',
            field=models.ForeignKey(verbose_name='likvidiral blago', to='partnerji.Oseba'),
        ),
        migrations.AddField(
            model_name='artikel',
            name='dobava',
            field=models.ManyToManyField(to='skladisce.Dobava', through='skladisce.Dnevnik'),
        ),
        migrations.AddField(
            model_name='artikel',
            name='dobavitelj',
            field=models.ForeignKey(to='partnerji.Partner'),
        ),
        migrations.AddField(
            model_name='artikel',
            name='tip',
            field=models.ForeignKey(to='skladisce.TipArtikla'),
        ),
    ]
