# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0008_auto_20151202_0047'),
        ('planiranje', '0013_planiranaaktivnost_planirano_opravilo'),
    ]

    operations = [
        migrations.AddField(
            model_name='planiranaaktivnost',
            name='artikel_plan',
            field=models.ForeignKey(null=True, to='katalog.ArtikelPlan', blank=True),
        ),
    ]
