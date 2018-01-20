# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kontrolnilist', '0023_remove_planaktivnost_osnova'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plankontrolaspecifikacija',
            name='plan_aktivnost',
        ),
    ]
