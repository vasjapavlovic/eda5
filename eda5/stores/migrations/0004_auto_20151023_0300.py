# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0003_auto_20151023_0259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icecreamstore',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
