# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pomanjkljivosti', '0002_auto_20170214_0951'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pomanjkljivost',
            old_name='element',
            new_name='elementx',
        ),
    ]
