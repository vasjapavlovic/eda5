# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planiranje', '0014_planiranaaktivnost_artikel_plan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planiranaaktivnost',
            name='naziv_opravila_izven_plana',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
