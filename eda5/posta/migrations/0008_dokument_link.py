# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import eda5.posta.models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0007_auto_20151220_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='dokument',
            name='link',
            field=models.CharField(max_length=500, default="ne_arhivirano", blank=True, null=True),
        ),
    ]
