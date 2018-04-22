# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KlasifikacijaDokumenta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('oznaka', models.CharField(max_length=100, null=True, blank=True)),
                ('oznaka_gen', models.CharField(max_length=100, null=True, blank=True)),
                ('naziv', models.CharField(max_length=255, null=True, blank=True)),
                ('opis', models.TextField(null=True, blank=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('zap_st', models.IntegerField(default=9999, verbose_name='zaporedna številka')),
                ('proces_oznaka', models.CharField(unique=True, max_length=10, verbose_name='Oznaka procesa')),
                ('proces_naziv', models.CharField(max_length=255, verbose_name='Naziv procesa')),
                ('postopek_oznaka', models.CharField(unique=True, max_length=10, verbose_name='Oznaka postopka')),
                ('postopek_naziv', models.CharField(max_length=255, verbose_name='Naziv postopka')),
                ('vrsta_dokumenta', models.ForeignKey(to='posta.VrstaDokumenta', verbose_name='Vrsta dokumenta')),
            ],
            options={
                'ordering': ('oznaka',),
                'verbose_name': 'Klasifikacija dokumenta',
                'verbose_name_plural': 'Klasifikacija dokumentov',
            },
        ),
    ]
