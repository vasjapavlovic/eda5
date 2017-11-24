# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogodki', '__first__'),
        ('zaznamki', '0004_zaznamek_razdelilnik'),
    ]

    operations = [
        migrations.AddField(
            model_name='zaznamek',
            name='dogodek',
            field=models.ForeignKey(null=True, to='dogodki.Dogodek', blank=True),
        ),
    ]
