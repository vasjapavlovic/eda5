# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arhiv', '0013_arhiviranje_dogodek'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arhiviranje',
            name='dogodek',
        ),
    ]
