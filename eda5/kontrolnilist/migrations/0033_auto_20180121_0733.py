# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kontrolnilist', '0032_auto_20180121_0731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kontrolaspecifikacija',
            name='vrednost_vrsta',
            field=models.IntegerField(default=1, verbose_name='vrsta vrednosti', choices=[(1, 'check'), (2, 'text'), (4, 'number'), (3, 'select')]),
        ),
    ]
