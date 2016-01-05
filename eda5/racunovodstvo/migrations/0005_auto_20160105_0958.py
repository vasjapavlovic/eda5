# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racunovodstvo', '0004_auto_20160105_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='strosek',
            name='is_strosek_posameznidel',
            field=models.NullBooleanField(verbose_name='strosek na posameznem delu'),
        ),
    ]
