# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lastnistvo', '0018_auto_20170120_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='najemlastnine',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='prodajalastnine',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
