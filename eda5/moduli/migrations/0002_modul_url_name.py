# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('moduli', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='modul',
            name='url_name',
            field=models.CharField(default='abc', max_length=10),
            preserve_default=False,
        ),
    ]
