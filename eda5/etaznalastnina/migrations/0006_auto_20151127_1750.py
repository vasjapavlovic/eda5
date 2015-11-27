# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etaznalastnina', '0005_auto_20151127_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lastniskaenotainterna',
            name='st_oseb',
            field=models.DecimalField(verbose_name='število oseb', max_digits=2, decimal_places=1, blank=True),
        ),
    ]
