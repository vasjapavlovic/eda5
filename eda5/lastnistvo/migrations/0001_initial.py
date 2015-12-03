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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('datum_predaje', models.DateField(verbose_name='datum predaje v najem')),
                ('trajanje_enota', models.CharField(verbose_name='enota trajanja najema', choices=[('dan', 'Dan'), ('teden', 'Teden'), ('mesec', 'Mesec'), ('leto', 'Leto')], max_length=5)),
                ('trajanje_kolicina', models.IntegerField(verbose_name='količina trajanja/enota')),
                ('placnik_stroskov', models.CharField(verbose_name='plačnik stroškov', choices=[(1, 'lastnik'), (2, 'najemnik')], max_length=8)),
            ],
            options={
                'verbose_name': 'najem',
                'verbose_name_plural': 'najem',
            },
        ),
        migrations.CreateModel(
            name='Prodaja',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('datum_predaje', models.DateField(verbose_name='datum predaje v posest')),
                ('datum_vpisa', models.DateField(verbose_name='datum vpisa v zemljiško knjigo', null=True, blank=True)),
            ],
            options={
                'verbose_name': 'prodaja',
                'verbose_name_plural': 'prodaja',
            },
        ),
    ]
