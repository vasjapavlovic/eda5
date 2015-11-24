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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_likvidiran', models.BooleanField(default=False)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.TextField(verbose_name='prijave - sporočilo')),
                ('prijavil', models.CharField(max_length=255)),
                ('datum_ugotovitve', models.DateField()),
                ('element', models.CharField(max_length=255)),
                ('etaza', models.CharField(max_length=50)),
                ('lokacija', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'pomanjkljivost',
                'verbose_name_plural': 'pomanjkljivosti',
            },
        ),
    ]
