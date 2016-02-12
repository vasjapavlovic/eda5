# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racunovodstvo', '0010_auto_20160107_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='strosek',
            name='osnova',
            field=models.DecimalField(max_digits=9, decimal_places=4, verbose_name='osnova za ddv'),
        ),
    ]
