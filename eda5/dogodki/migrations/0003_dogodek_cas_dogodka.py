# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogodki', '0002_auto_20161101_0644'),
    ]

    operations = [
        migrations.AddField(
            model_name='dogodek',
            name='cas_dogodka',
            field=models.TimeField(verbose_name='okvirni čas dogodka', null=True, blank=True),
        ),
    ]
