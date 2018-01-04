# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modul',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('zap_st', models.IntegerField(verbose_name='zaporedna številka', default=9999)),
                ('oznaka', models.CharField(max_length=10, unique=True)),
                ('naziv', models.CharField(max_length=200)),
                ('opis', models.TextField()),
                ('barva', models.CharField(max_length=500)),
                ('url_ref', models.CharField(max_length=500, blank=True)),
            ],
            options={
                'verbose_name': 'modul',
                'ordering': ['zap_st', 'naziv'],
                'verbose_name_plural': 'moduli',
            },
        ),
        migrations.CreateModel(
            name='Zavihek',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('zap_st', models.IntegerField(verbose_name='zaporedna številka', default=9999)),
                ('oznaka', models.CharField(max_length=100, unique=True)),
                ('naziv', models.CharField(max_length=200)),
                ('url_ref', models.CharField(max_length=500, blank=True)),
                ('modul', models.ForeignKey(to='moduli.Modul')),
                ('parent', models.ManyToManyField(to='moduli.Zavihek', blank=True, related_name='_parent_+')),
            ],
            options={
                'verbose_name': 'zavihek',
                'ordering': ['zap_st', 'oznaka'],
                'verbose_name_plural': 'zavihki',
            },
        ),
    ]
