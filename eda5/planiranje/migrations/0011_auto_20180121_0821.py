# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planiranje', '0010_auto_20180121_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plankontrolaspecifikacija',
            name='vrednost_vrsta',
            field=models.IntegerField(default=1, verbose_name='vrsta vrednosti', choices=[(1, 'check'), (2, 'text'), (4, 'number'), (5, 'yes_no'), (3, 'select')]),
        ),
    ]
