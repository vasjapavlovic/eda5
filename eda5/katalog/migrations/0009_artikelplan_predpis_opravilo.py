# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predpisi', '0001_initial'),
        ('katalog', '0008_auto_20151202_0047'),
    ]

    operations = [
        migrations.AddField(
            model_name='artikelplan',
            name='predpis_opravilo',
            field=models.ForeignKey(null=True, blank=True, to='predpisi.PredpisOpravilo'),
        ),
    ]
