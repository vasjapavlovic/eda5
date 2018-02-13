# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pomanjkljivosti', '0004_auto_20180213_1328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pomanjkljivost',
            name='gradivo',
        ),
        migrations.RemoveField(
            model_name='pomanjkljivost',
            name='gradivo_zaznamek',
        ),
    ]
