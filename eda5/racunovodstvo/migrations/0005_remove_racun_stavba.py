# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racunovodstvo', '0004_auto_20170802_1839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='racun',
            name='stavba',
        ),
    ]
