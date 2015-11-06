# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racunovodstvo', '0008_auto_20151029_1501'),
        ('delovninalogi', '0004_auto_20151101_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='delovninalog',
            name='strosek',
            field=models.ForeignKey(to='racunovodstvo.Strosek', null=True, blank=True),
        ),
    ]
