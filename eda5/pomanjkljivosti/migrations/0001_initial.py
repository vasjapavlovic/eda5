# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pomanjkljivost',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.TextField(verbose_name='prijave - sporočilo')),
                ('prijavil', models.CharField(max_length=255)),
                ('element', models.CharField(max_length=255)),
                ('lokacija', models.CharField(max_length=255)),
                ('datum_ugotovitve', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'pomanjkljivosti',
                'verbose_name': 'pomanjkljivost',
            },
        ),
    ]
