# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arhiv', '0008_auto_20160105_1920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arhiviranje',
            name='zahtevek',
        ),
    ]
