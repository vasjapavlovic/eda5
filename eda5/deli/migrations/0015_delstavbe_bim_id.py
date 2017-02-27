# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0014_auto_20170227_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='delstavbe',
            name='bim_id',
            field=models.CharField(verbose_name='BIM ID', max_length=100, null=True, blank=True),
        ),
    ]
