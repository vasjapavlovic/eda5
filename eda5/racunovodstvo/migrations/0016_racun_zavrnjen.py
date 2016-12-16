# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racunovodstvo', '0015_auto_20161216_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='racun',
            name='zavrnjen',
            field=models.BooleanField(default=False),
        ),
    ]
