# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lastnistvo', '0020_auto_20170129_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='najemlastnine',
            name='is_likvidiran',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='prodajalastnine',
            name='is_likvidiran',
            field=models.BooleanField(default=False),
        ),
    ]
