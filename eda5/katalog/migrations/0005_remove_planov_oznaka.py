# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0004_planov_plan_opravilo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planov',
            name='oznaka',
        ),
    ]
