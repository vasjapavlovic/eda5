# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0004_auto_20161118_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='projektnomesto',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='projektnomesto',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='projektnomesto',
            name='updated',
            field=models.DateTimeField(null=True, auto_now=True),
        ),
    ]
