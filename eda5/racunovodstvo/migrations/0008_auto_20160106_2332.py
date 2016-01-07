# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racunovodstvo', '0007_auto_20160105_2238'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='racun',
            options={'ordering': ['racunovodsko_leto', 'oznaka'], 'verbose_name_plural': 'računi', 'verbose_name': 'račun'},
        ),
    ]
