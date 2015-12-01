# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planiranje', '0003_auto_20151201_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='planizdaja',
            name='oznaka',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]
