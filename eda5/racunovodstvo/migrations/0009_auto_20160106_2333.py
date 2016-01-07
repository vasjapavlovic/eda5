# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racunovodstvo', '0008_auto_20160106_2332'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='racun',
            options={'verbose_name': 'račun', 'verbose_name_plural': 'računi', 'ordering': ('-racunovodsko_leto', '-oznaka')},
        ),
    ]
