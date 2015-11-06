# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delovninalogi', '0005_delovninalog_strosek'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delovninalog',
            name='strosek',
        ),
    ]
