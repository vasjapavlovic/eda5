# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planiranje', '0012_planiranaaktivnost_element'),
    ]

    operations = [
        migrations.AddField(
            model_name='planiranaaktivnost',
            name='planirano_opravilo',
            field=models.ForeignKey(to='planiranje.PlaniranoOpravilo', null=True, blank=True),
        ),
    ]
