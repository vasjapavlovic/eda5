# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obvestila', '0004_auto_20160222_0813'),
    ]

    operations = [
        migrations.AddField(
            model_name='obvestilo',
            name='objavljeno',
            field=models.BooleanField(default=False),
        ),
    ]
