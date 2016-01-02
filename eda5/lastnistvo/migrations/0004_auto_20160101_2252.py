# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lastnistvo', '0003_auto_20160101_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predajalastnine',
            name='placnik_stroskov',
            field=models.IntegerField(blank=True, choices=[(1, 'lastnik'), (2, 'najemnik'), (3, 'podnajemnik')], null=True, verbose_name='plačnik stroškov'),
        ),
        migrations.AlterField(
            model_name='predajalastnine',
            name='vrsta_predaje',
            field=models.IntegerField(choices=[(1, 'predaja v last'), (2, 'predaja v najem'), (3, 'predaja v podnajem')]),
        ),
    ]
