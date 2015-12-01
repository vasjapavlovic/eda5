# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planiranje', '0003_auto_20151201_1853'),
        ('katalog', '0003_remove_modelartikla_oznaka'),
    ]

    operations = [
        migrations.AddField(
            model_name='planov',
            name='plan_opravilo',
            field=models.ForeignKey(null=True, blank=True, to='planiranje.PlanOpravilo'),
        ),
    ]
