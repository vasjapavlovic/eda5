# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('razdelilnik', '0003_auto_20151029_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='strosekle',
            name='delilnik_vrednost',
            field=models.DecimalField(decimal_places=4, default=10, max_digits=8),
            preserve_default=False,
        ),
    ]
