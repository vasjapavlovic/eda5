# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etaznalastnina', '0015_auto_20151219_0936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='internadodatno',
            name='lastnik',
        ),
        migrations.RemoveField(
            model_name='internadodatno',
            name='najemnik',
        ),
        migrations.RemoveField(
            model_name='internadodatno',
            name='placnik',
        ),
    ]
