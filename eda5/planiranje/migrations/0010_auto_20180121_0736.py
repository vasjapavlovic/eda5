# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planiranje', '0009_auto_20180119_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plankontrolaspecifikacija',
            name='vrednost_vrsta',
            field=models.IntegerField(choices=[(1, 'check'), (2, 'text'), (4, 'number'), (3, 'select')], default=1, verbose_name='vrsta vrednosti'),
        ),
    ]
