# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racunovodstvo', '0007_auto_20170805_1440'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='strosek',
            options={'verbose_name_plural': 'stroški', 'ordering': ('-racun__racunovodsko_leto', '-racun__oznaka', 'oznaka'), 'verbose_name': 'strošek'},
        ),
    ]
