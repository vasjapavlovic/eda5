# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pomanjkljivosti', '0005_auto_20180213_1414'),
        ('zaznamki', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='zaznamek',
            name='pomanjkljivost',
            field=models.ForeignKey(blank=True, null=True, to='pomanjkljivosti.Pomanjkljivost'),
        ),
    ]
