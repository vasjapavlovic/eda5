# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0006_auto_20151026_0359'),
    ]

    operations = [
        migrations.AddField(
            model_name='dokument',
            name='likvidiran',
            field=models.BooleanField(default=False),
        ),
    ]
