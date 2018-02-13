# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pomanjkljivosti', '0003_auto_20180213_1321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pomanjkljivost',
            name='delovninalog',
        ),
        migrations.RemoveField(
            model_name='pomanjkljivost',
            name='dogodek',
        ),
    ]
