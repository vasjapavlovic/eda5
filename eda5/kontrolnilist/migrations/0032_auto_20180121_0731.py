# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kontrolnilist', '0031_auto_20180121_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kontrolaspecifikacija',
            name='vrednost_vrsta',
            field=models.IntegerField(verbose_name='vrsta vrednosti', choices=[(1, 'check'), (2, 'text'), (2, 'number'), (3, 'select')], default=1),
        ),
    ]
