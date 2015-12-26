# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planiranje', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='planiranoopravilo',
            options={'ordering': ('oznaka',), 'verbose_name_plural': 'planirana opravila', 'verbose_name': 'planirano opravilo'},
        ),
    ]
