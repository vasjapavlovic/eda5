# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planiranje', '0007_auto_20180119_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='planaktivnost',
            name='zap_st',
            field=models.IntegerField(default=9999, verbose_name='zaporedna številka'),
        ),
    ]
