# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0016_auto_20170227_1147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delstavbe',
            name='shema',
        ),
    ]
