# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racunovodstvo', '0020_racun_opravilo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='racun',
            name='opravilo',
        ),
    ]
