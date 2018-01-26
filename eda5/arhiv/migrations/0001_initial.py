# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0001_initial'),
        ('partnerji', '0001_initial'),
        ('zahtevki', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arhiv',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('oznaka', models.CharField(verbose_name='oznaka', max_length=50, unique=True)),
                ('naziv', models.CharField(verbose_name='naziv', max_length=255)),
            ],
            options={
                'verbose_name_plural': 'arhivi',
                'verbose_name': 'arhiv',
            },
        ),
        migrations.CreateModel(
            name='Arhiviranje',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('elektronski', models.BooleanField(default=True, verbose_name='elektronski hramba')),
                ('fizicni', models.BooleanField(default=False, verbose_name='fizični hramba')),
                ('arhiviral', models.ForeignKey(to='partnerji.Oseba')),
                ('artikel', models.ForeignKey(null=True, blank=True, to='katalog.ModelArtikla')),
            ],
            options={
                'verbose_name_plural': 'arhiviranje',
                'verbose_name': 'arhiviranje',
            },
        ),
        migrations.CreateModel(
            name='ArhivMesto',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('oznaka', models.CharField(verbose_name='oznaka', max_length=50)),
                ('naziv', models.CharField(verbose_name='naziv', max_length=255)),
                ('arhiv', models.ForeignKey(to='arhiv.Arhiv')),
                ('zahtevek', models.OneToOneField(null=True, blank=True, to='zahtevki.Zahtevek')),
            ],
            options={
                'verbose_name_plural': 'arhivska mesta',
                'verbose_name': 'arhivsko mesto',
            },
        ),
    ]
