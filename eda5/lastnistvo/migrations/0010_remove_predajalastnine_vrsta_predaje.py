# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lastnistvo', '0009_auto_20160102_0027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='predajalastnine',
            name='vrsta_predaje',
        ),
    ]
