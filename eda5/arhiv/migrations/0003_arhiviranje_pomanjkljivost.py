# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pomanjkljivosti', '0005_auto_20180213_1414'),
        ('arhiv', '0002_auto_20180126_2341'),
    ]

    operations = [
        migrations.AddField(
            model_name='arhiviranje',
            name='pomanjkljivost',
            field=models.ForeignKey(blank=True, to='pomanjkljivosti.Pomanjkljivost', null=True),
        ),
    ]
