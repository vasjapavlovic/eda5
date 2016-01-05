# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0013_auto_20151231_0819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aktivnost',
            name='likvidiral',
        ),
    ]
