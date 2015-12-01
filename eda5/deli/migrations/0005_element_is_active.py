# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0004_auto_20151127_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='element',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
