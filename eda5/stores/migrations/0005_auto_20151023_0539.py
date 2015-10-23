# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0004_auto_20151023_0300'),
    ]

    operations = [
        migrations.AddField(
            model_name='icecreamstore',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 10, 23, 3, 39, 25, 145589, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='icecreamstore',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 23, 3, 39, 30, 105039, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
