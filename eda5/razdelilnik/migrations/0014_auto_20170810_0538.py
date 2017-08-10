# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('razdelilnik', '0013_auto_20170805_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='razdelilnik',
            name='oznaka_gen',
            field=models.CharField(null=True, max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='razdelilnik',
            name='oznaka',
            field=models.CharField(null=True, max_length=20, blank=True),
        ),
    ]
