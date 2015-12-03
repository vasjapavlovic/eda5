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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('st_pogodbe', models.CharField(verbose_name='številka pogodbe', max_length=20)),
                ('predmet_pogodbe', models.CharField(verbose_name='številka pogodbe', max_length=255)),
            ],
            options={
                'verbose_name': 'pogodbeno naročilo',
                'verbose_name_plural': 'pogodbena naročila',
            },
        ),
        migrations.CreateModel(
            name='NarociloTelefon',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
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
