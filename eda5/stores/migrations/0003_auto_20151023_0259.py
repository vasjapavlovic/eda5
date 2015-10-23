# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_auto_20151023_0259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icecreamstore',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
