# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0018_auto_20170227_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projektnomesto',
            name='bim_id',
            field=models.CharField(null=True, blank=True, max_length=100, verbose_name='BIM ID'),
        ),
    ]
