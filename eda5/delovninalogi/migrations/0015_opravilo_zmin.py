# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delovninalogi', '0014_auto_20170221_0847'),
    ]

    operations = [
        migrations.AddField(
            model_name='opravilo',
            name='zmin',
            field=models.IntegerField(default=15, verbose_name='zaokrožitev [min]'),
        ),
    ]
