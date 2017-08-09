# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('razdelilnik', '0011_auto_20170805_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='strosekrazdelilnikpostavka',
            name='delilnik_vrednost',
            field=models.DecimalField(decimal_places=4, max_digits=8, default=0.8),
            preserve_default=False,
        ),
    ]
