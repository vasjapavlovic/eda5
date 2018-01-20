# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kontrolnilist', '0017_plankontrolaspecifikacijaopcijaselect'),
    ]

    operations = [
        migrations.CreateModel(
            name='KontrolaSkupina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('oznaka', models.CharField(null=True, max_length=100, blank=True)),
                ('oznaka_gen', models.CharField(null=True, max_length=100, blank=True)),
                ('naziv', models.CharField(null=True, max_length=255, blank=True)),
                ('opis', models.TextField(null=True, blank=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('status', models.IntegerField(choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')], default=0)),
            ],
            options={
                'verbose_name': 'Skupina kontrol',
                'ordering': ['oznaka'],
            },
        ),
        migrations.CreateModel(
            name='PlanKontrolaSkupina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('oznaka', models.CharField(null=True, max_length=100, blank=True)),
                ('oznaka_gen', models.CharField(null=True, max_length=100, blank=True)),
                ('naziv', models.CharField(null=True, max_length=255, blank=True)),
                ('opis', models.TextField(null=True, blank=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
                ('status', models.IntegerField(choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')], default=0)),
            ],
            options={
                'verbose_name': 'Skupina planiranih kontrol',
                'ordering': ['oznaka'],
            },
        ),
        migrations.AddField(
            model_name='kontrolaspecifikacija',
            name='kontrola_skupina',
            field=models.ForeignKey(verbose_name='skupina kontrol', null=True, to='kontrolnilist.KontrolaSkupina', blank=True),
        ),
        migrations.AddField(
            model_name='plankontrolaspecifikacija',
            name='plan_kontrola_skupina',
            field=models.ForeignKey(verbose_name='skupina planiranih kontrol', null=True, to='kontrolnilist.PlanKontrolaSkupina', blank=True),
        ),
    ]
