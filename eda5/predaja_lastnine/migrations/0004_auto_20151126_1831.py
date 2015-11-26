# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predaja_lastnine', '0003_auto_20151126_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predajalastnine',
            name='tip_predaje',
            field=models.CharField(max_length=1, choices=[('P', 'predaja v last'), ('N', 'predaja v najem')], verbose_name='tip predaje etažne lastnine'),
        ),
    ]
