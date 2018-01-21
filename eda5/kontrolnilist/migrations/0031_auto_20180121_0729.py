# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kontrolnilist', '0030_auto_20180121_0725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kontrolaspecifikacija',
            name='vrednost_vrsta',
            field=models.IntegerField(choices=[(1, 'check'), (2, 'text'), (3, 'select')], verbose_name='vrsta vrednosti', default=1),
        ),
    ]
