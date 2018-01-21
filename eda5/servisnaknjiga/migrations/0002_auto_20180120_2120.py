# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0004_delstavbe_stavba'),
        ('planiranje', '0009_auto_20180119_1729'),
        ('servisnaknjiga', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('oznaka', models.CharField(null=True, max_length=100, blank=True)),
                ('oznaka_gen', models.CharField(null=True, max_length=100, blank=True)),
                ('naziv', models.CharField(null=True, max_length=255, blank=True)),
                ('opis', models.TextField(null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'v čakanju'), (2, 'v planu'), (3, 'v reševanju'), (4, 'zaključeno'), (5, 'izbrisano'), (6, 'neaktivno')])),
                ('plan_kontrola_specifikacija', models.ForeignKey(to='planiranje.PlanKontrolaSpecifikacija', verbose_name='poročilo o rezultatu kontrole')),
                ('projektno_mesto', models.ForeignKey(to='deli.ProjektnoMesto', verbose_name='projektno mesto')),
            ],
            options={
                'verbose_name': 'Report maped PlanKontrolaSpeciikacija',
            },
        ),
        migrations.RemoveField(
            model_name='reportplankontrolaspecifikacija',
            name='plan_kontrola_specifikacija',
        ),
        migrations.DeleteModel(
            name='ReportPlanKontrolaSpecifikacija',
        ),
    ]
