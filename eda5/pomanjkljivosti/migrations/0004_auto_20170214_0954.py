# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pomanjkljivosti', '0003_auto_20170214_0952'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pomanjkljivost',
            old_name='elementx',
            new_name='element',
        ),
    ]
