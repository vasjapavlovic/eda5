# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predpisi', '0001_initial'),
        ('kontrolnilist', '0021_auto_20180117_0710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planaktivnost',
            name='predpis_opravilo',
        ),
        migrations.AddField(
            model_name='planaktivnost',
            name='osnova',
            field=models.ForeignKey(to='predpisi.PredpisSklop', null=True, blank=True),
        ),
    ]
