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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('datum_predaje', models.DateField(verbose_name='datum predaje v najem')),
                ('trajanje_enota', models.CharField(choices=[('dan', 'Dan'), ('teden', 'Teden'), ('mesec', 'Mesec'), ('leto', 'Leto')], max_length=5, verbose_name='enota trajanja najema')),
                ('trajanje_kolicina', models.IntegerField(verbose_name='količina trajanja/enota')),
                ('placnik_stroskov', models.CharField(choices=[(1, 'lastnik'), (2, 'najemnik')], max_length=8, verbose_name='plačnik stroškov')),
            ],
            options={
                'verbose_name_plural': 'najem',
                'verbose_name': 'najem',
            },
        ),
        migrations.CreateModel(
            name='Prodaja',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('datum_predaje', models.DateField(verbose_name='datum predaje v posest')),
                ('datum_vpisa', models.DateField(blank=True, null=True, verbose_name='datum vpisa v zemljiško knjigo')),
            ],
            options={
                'verbose_name_plural': 'prodaja',
                'verbose_name': 'prodaja',
            },
        ),
    ]
