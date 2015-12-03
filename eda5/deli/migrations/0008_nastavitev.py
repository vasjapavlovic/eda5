# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0010_obratovalniparameter'),
        ('deli', '0007_auto_20151201_1847'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nastavitev',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('datum_nastavitve', models.DateField()),
                ('vrednost', models.CharField(max_length=20)),
                ('element', models.ForeignKey(to='deli.Element')),
                ('obratovalni_parameter', models.ForeignKey(to='katalog.ObratovalniParameter')),
            ],
            options={
                'verbose_name_plural': 'nastavitve',
                'verbose_name': 'nastavitev',
            },
        ),
    ]
