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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('zap_st', models.IntegerField(verbose_name='zaporedna številka', default=9999)),
                ('oznaka', models.CharField(max_length=10, unique=True)),
                ('naziv', models.CharField(max_length=200)),
                ('opis', models.TextField()),
                ('barva', models.CharField(max_length=500)),
                ('url_ref', models.CharField(blank=True, max_length=500)),
            ],
            options={
                'verbose_name_plural': 'moduli',
                'verbose_name': 'modul',
                'ordering': ['zap_st', 'naziv'],
            },
        ),
        migrations.CreateModel(
            name='Zavihek',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('zap_st', models.IntegerField(verbose_name='zaporedna številka', default=9999)),
                ('oznaka', models.CharField(max_length=100, unique=True)),
                ('naziv', models.CharField(max_length=200)),
                ('url_ref', models.CharField(blank=True, max_length=500)),
                ('modul', models.ForeignKey(to='moduli.Modul')),
                ('parent', models.ManyToManyField(blank=True, related_name='_parent_+', to='moduli.Zavihek')),
            ],
            options={
                'verbose_name_plural': 'zavihki',
                'verbose_name': 'zavihek',
                'ordering': ['zap_st', 'oznaka'],
            },
        ),
    ]
