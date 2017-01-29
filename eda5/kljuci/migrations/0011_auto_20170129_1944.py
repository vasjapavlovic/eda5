# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kljuci', '0010_auto_20170111_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='predajakljuca',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='predajakljuca',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
