# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planiranje', '0002_planiranoopravilo_aktivnost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planiranoopravilo',
            name='aktivnost',
        ),
    ]
