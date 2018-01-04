# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ObrazecSplosno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('oznaka', models.CharField(verbose_name='Oznaka Dokumenta', max_length=100)),
                ('objava', models.DateTimeField(verbose_name='Datum Objave Dokumenta', null=True, blank=True)),
                ('zadeva', models.CharField(verbose_name='Zadeva Dopisa', max_length=255)),
                ('vsebina', models.TextField(verbose_name='Vsebina Dopisa')),
            ],
            options={
                'verbose_name_plural': 'Obrazec Splošno',
            },
        ),
    ]
