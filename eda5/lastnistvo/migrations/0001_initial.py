# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Najem',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('datum_predaje', models.DateField(verbose_name='datum predaje v najem')),
                ('trajanje_enota', models.CharField(max_length=5, choices=[('dan', 'Dan'), ('teden', 'Teden'), ('mesec', 'Mesec'), ('leto', 'Leto')], verbose_name='enota trajanja najema')),
                ('trajanje_kolicina', models.IntegerField(verbose_name='količina trajanja/enota')),
                ('placnik_stroskov', models.CharField(max_length=8, choices=[(1, 'lastnik'), (2, 'najemnik')], verbose_name='plačnik stroškov')),
            ],
            options={
                'verbose_name': 'najem',
                'verbose_name_plural': 'najem',
            },
        ),
        migrations.CreateModel(
            name='Prodaja',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('datum_predaje', models.DateField(verbose_name='datum predaje v posest')),
                ('datum_vpisa', models.DateField(verbose_name='datum vpisa v zemljiško knjigo', blank=True, null=True)),
            ],
            options={
                'verbose_name': 'prodaja',
                'verbose_name_plural': 'prodaja',
            },
        ),
    ]
