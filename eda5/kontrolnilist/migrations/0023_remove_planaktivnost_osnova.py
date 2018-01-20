# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kontrolnilist', '0022_auto_20180117_0723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planaktivnost',
            name='osnova',
        ),
    ]
