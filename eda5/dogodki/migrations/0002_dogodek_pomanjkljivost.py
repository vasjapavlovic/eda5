# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pomanjkljivosti', '0005_auto_20180213_1414'),
        ('dogodki', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dogodek',
            name='pomanjkljivost',
            field=models.ManyToManyField(to='pomanjkljivosti.Pomanjkljivost', blank=True),
        ),
    ]
