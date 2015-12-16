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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('predmet', models.CharField(max_length=255)),
                ('datum_narocila', models.DateField(verbose_name='datum naročila')),
                ('datum_veljavnosti', models.DateField(verbose_name='velja do')),
                ('vrednost', models.DecimalField(max_digits=7, decimal_places=2)),
            ],
            options={
                'verbose_name_plural': 'naročila',
                'verbose_name': 'naročilo',
            },
        ),
        migrations.CreateModel(
            name='NarociloPogodba',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('st_pogodbe', models.CharField(max_length=20, verbose_name='številka pogodbe')),
                ('predmet_pogodbe', models.CharField(max_length=255, verbose_name='številka pogodbe')),
            ],
            options={
                'verbose_name_plural': 'pogodbena naročila',
                'verbose_name': 'pogodbeno naročilo',
            },
        ),
        migrations.CreateModel(
            name='NarociloTelefon',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('telefonska_stevilka', models.CharField(max_length=20)),
                ('datum_klica', models.DateField()),
                ('cas_klica', models.TimeField()),
                ('telefonsko_sporocilo', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'naročila po telefonu',
                'verbose_name': 'naročilo po telefonu',
            },
        ),
    ]
