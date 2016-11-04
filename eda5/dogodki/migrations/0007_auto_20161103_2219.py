# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogodki', '0006_auto_20161103_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dogodek',
            name='povzrocitelj',
            field=models.CharField(verbose_name='povzročitelj (opisno)', max_length=255, blank=True),
        ),
    ]
