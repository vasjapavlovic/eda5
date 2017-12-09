# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0001_initial'),
        ('zahtevki', '__first__'),
        ('delovninalogi', '__first__'),
        ('partnerji', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arhiv',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('oznaka', models.CharField(verbose_name='oznaka', unique=True, max_length=50)),
                ('naziv', models.CharField(verbose_name='naziv', max_length=255)),
            ],
            options={
                'verbose_name': 'arhiv',
                'verbose_name_plural': 'arhivi',
            },
        ),
        migrations.CreateModel(
            name='Arhiviranje',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('elektronski', models.BooleanField(default=True, verbose_name='elektronski hramba')),
                ('fizicni', models.BooleanField(default=False, verbose_name='fizični hramba')),
                ('arhiviral', models.ForeignKey(to='partnerji.Oseba')),
                ('artikel', models.ForeignKey(null=True, blank=True, to='katalog.ModelArtikla')),
                ('delovninalog', models.ForeignKey(null=True, blank=True, to='delovninalogi.DelovniNalog')),
            ],
            options={
                'verbose_name': 'arhiviranje',
                'verbose_name_plural': 'arhiviranje',
            },
        ),
        migrations.CreateModel(
            name='ArhivMesto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('oznaka', models.CharField(verbose_name='oznaka', max_length=50)),
                ('naziv', models.CharField(verbose_name='naziv', max_length=255)),
                ('arhiv', models.ForeignKey(to='arhiv.Arhiv')),
                ('zahtevek', models.OneToOneField(null=True, to='zahtevki.Zahtevek', blank=True)),
            ],
            options={
                'verbose_name': 'arhivsko mesto',
                'verbose_name_plural': 'arhivska mesta',
            },
        ),
    ]
