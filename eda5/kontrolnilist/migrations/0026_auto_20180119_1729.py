# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0004_delstavbe_stavba'),
        ('planiranje', '0009_auto_20180119_1729'),
        ('kontrolnilist', '0025_auto_20180118_1701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aktivnost',
            name='projektno_mesto',
        ),
        migrations.AddField(
            model_name='kontrolaspecifikacija',
            name='plan_kontrola_specifikacija',
            field=models.ForeignKey(to='planiranje.PlanKontrolaSpecifikacija', verbose_name='planirana kontrola specifikacija', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kontrolaspecifikacija',
            name='projektno_mesto',
            field=models.ManyToManyField(to='deli.ProjektnoMesto', verbose_name='projektno mesto', blank=True),
        ),
    ]
