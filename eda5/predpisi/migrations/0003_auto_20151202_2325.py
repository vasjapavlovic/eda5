# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predpisi', '0002_auto_20151202_2040'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='predpisopravilo',
            options={'verbose_name_plural': 'predpisana opravila', 'verbose_name': 'predpisano opravilo'},
        ),
    ]
