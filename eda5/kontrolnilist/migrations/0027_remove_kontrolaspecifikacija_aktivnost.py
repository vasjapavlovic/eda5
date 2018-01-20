# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kontrolnilist', '0026_auto_20180119_1729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kontrolaspecifikacija',
            name='aktivnost',
        ),
    ]
