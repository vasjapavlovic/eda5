# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pomanjkljivosti', '0002_pomanjkljivost_etaza'),
    ]

    operations = [
        migrations.AddField(
            model_name='pomanjkljivost',
            name='is_likvidiran',
            field=models.BooleanField(default=False),
        ),
    ]
