# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0005_auto_20170112_1416'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partner',
            name='skupina_partnerja',
        ),
    ]
