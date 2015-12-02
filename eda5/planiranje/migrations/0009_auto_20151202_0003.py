# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planiranje', '0008_auto_20151202_0002'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SklopPlanov',
            new_name='SkupinaPlanov',
        ),
        migrations.AlterModelOptions(
            name='skupinaplanov',
            options={'verbose_name_plural': 'skupine planov', 'ordering': ('zap_st',), 'verbose_name': 'skupina planov'},
        ),
    ]
