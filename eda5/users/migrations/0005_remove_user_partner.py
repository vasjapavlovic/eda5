# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20151029_1714'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='partner',
        ),
    ]
