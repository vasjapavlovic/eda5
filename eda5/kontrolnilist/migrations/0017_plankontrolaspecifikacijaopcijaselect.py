# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kontrolnilist', '0016_planaktivnost_plankontrolaspecifikacija'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanKontrolaSpecifikacijaOpcijaSelect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('oznaka', models.CharField(max_length=100, null=True, blank=True)),
                ('oznaka_gen', models.CharField(max_length=100, null=True, blank=True)),
                ('naziv', models.CharField(max_length=255, null=True, blank=True)),
                ('opis', models.TextField(null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('plan_kontrola_specifikacija', models.ForeignKey(verbose_name='specifikacija planirane kontrole', to='kontrolnilist.PlanKontrolaSpecifikacija')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
