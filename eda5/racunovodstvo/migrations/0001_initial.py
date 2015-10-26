# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0007_dokument_likvidiran'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DavcnaKlasifikacija',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('oznaka', models.CharField(max_length=10)),
                ('naziv', models.CharField(max_length=50)),
                ('opis', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'davčna klasifikacija',
                'verbose_name_plural': 'davčna klasifikacija',
            },
        ),
        migrations.CreateModel(
            name='Racun',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('datum_storitve_od', models.DateField()),
                ('datum_storitve_do', models.DateField()),
                ('davcna_klasifikacija', models.ForeignKey(to='racunovodstvo.DavcnaKlasifikacija')),
                ('dokument', models.ForeignKey(to='posta.Dokument')),
                ('obdobje_obracuna_leto', models.ForeignKey(to='core.ObdobjeLeto')),
                ('obdobje_obracuna_mesec', models.ForeignKey(to='core.ObdobjeMesec')),
            ],
            options={
                'verbose_name': 'račun',
                'verbose_name_plural': 'računi',
            },
        ),
    ]
