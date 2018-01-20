# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predpisi', '0001_initial'),
        ('kontrolnilist', '0020_auto_20180116_0755'),
    ]

    operations = [
        migrations.AddField(
            model_name='aktivnost',
            name='plan_aktivnost',
            field=models.ForeignKey(to='kontrolnilist.PlanAktivnost', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='planaktivnost',
            name='predpis_opravilo',
            field=models.ForeignKey(to='predpisi.PredpisOpravilo', null=True, blank=True),
        ),
    ]
