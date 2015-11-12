# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0010_auto_20151111_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='dokument',
            name='datum',
            field=models.DateField(default=datetime.datetime(2015, 11, 12, 9, 43, 12, 274684, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
