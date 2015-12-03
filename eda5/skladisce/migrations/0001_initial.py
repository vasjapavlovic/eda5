# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delovninalogi', '0001_initial'),
        ('partnerji', '0001_initial'),
        ('posta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artikel',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('oznaka', models.CharField(max_length=50)),
                ('naziv', models.CharField(max_length=255)),
                ('opis', models.CharField(max_length=255, blank=True)),
                ('st_police', models.IntegerField(verbose_name='številka police', null=True, blank=True)),
            ],
            options={
                'verbose_name': 'artikel',
                'verbose_name_plural': 'artikli',
            },
        ),
        migrations.CreateModel(
            name='Dnevnik',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('kom', models.IntegerField()),
                ('cena', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('stopnja_ddv', models.DecimalField(null=True, max_digits=4, decimal_places=3, blank=True)),
                ('artikel', models.ForeignKey(to='skladisce.Artikel')),
                ('delovninalog', models.ForeignKey(to='delovninalogi.DelovniNalog', null=True, verbose_name='delovni nalog', blank=True)),
            ],
            options={
                'verbose_name': 'dnevnik',
                'verbose_name_plural': 'dnevnik',
            },
        ),
        migrations.CreateModel(
            name='Dobava',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
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
                'verbose_name': 'dobava',
                'verbose_name_plural': 'dobave',
            },
        ),
        migrations.CreateModel(
            name='SklopArtikla',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('oznaka', models.CharField(max_length=50)),
                ('naziv', models.CharField(max_length=255)),
                ('opis', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'verbose_name': 'sklop artikla',
                'verbose_name_plural': 'sklopi artiklov',
            },
        ),
        migrations.CreateModel(
            name='TipArtikla',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('oznaka', models.CharField(max_length=50)),
                ('naziv', models.CharField(max_length=255)),
                ('opis', models.CharField(max_length=255, blank=True)),
                ('sklop', models.ForeignKey(to='skladisce.SklopArtikla')),
            ],
            options={
                'verbose_name': 'tip artikla',
                'verbose_name_plural': 'tipi artiklov',
            },
        ),
        migrations.AddField(
            model_name='dnevnik',
            name='dobava',
            field=models.ForeignKey(to='skladisce.Dobava', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='dnevnik',
            name='likvidiral',
            field=models.ForeignKey(to='partnerji.Oseba', verbose_name='likvidiral blago'),
        ),
        migrations.AddField(
            model_name='artikel',
            name='dobava',
            field=models.ManyToManyField(through='skladisce.Dnevnik', to='skladisce.Dobava'),
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
