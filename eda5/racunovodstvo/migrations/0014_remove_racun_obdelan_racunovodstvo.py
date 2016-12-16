# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racunovodstvo', '0013_auto_20161216_1656'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='racun',
            name='obdelan_racunovodstvo',
        ),
    ]
