# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delovninalogi', '0009_auto_20180105_1216'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpcijeSelect',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('oznaka', models.CharField(blank=True, null=True, max_length=100)),
                ('oznaka_gen', models.CharField(blank=True, null=True, max_length=100)),
                ('naziv', models.CharField(blank=True, null=True, max_length=255)),
                ('opis', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('aktivnost_parameter_specifikacija', models.ForeignKey(verbose_name='opcija izbire', to='delovninalogi.AktivnostParameterSpecifikacija')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
