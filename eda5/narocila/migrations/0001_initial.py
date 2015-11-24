# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Narocilo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('predmet', models.CharField(max_length=255)),
                ('datum_narocila', models.DateField(verbose_name='datum naročila')),
                ('datum_veljavnosti', models.DateField(verbose_name='velja do')),
                ('vrednost', models.DecimalField(max_digits=7, decimal_places=2)),
            ],
            options={
                'verbose_name': 'naročilo',
                'verbose_name_plural': 'naročila',
            },
        ),
        migrations.CreateModel(
            name='NarociloPogodba',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('st_pogodbe', models.CharField(max_length=20, verbose_name='številka pogodbe')),
                ('predmet_pogodbe', models.CharField(max_length=255, verbose_name='številka pogodbe')),
            ],
            options={
                'verbose_name': 'pogodbeno naročilo',
                'verbose_name_plural': 'pogodbena naročila',
            },
        ),
        migrations.CreateModel(
            name='NarociloTelefon',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('telefonska_stevilka', models.CharField(max_length=20)),
                ('datum_klica', models.DateField()),
                ('cas_klica', models.TimeField()),
                ('telefonsko_sporocilo', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'naročilo po telefonu',
                'verbose_name_plural': 'naročila po telefonu',
            },
        ),
    ]
