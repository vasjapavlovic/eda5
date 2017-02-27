# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0017_remove_delstavbe_shema'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projektnomesto',
            name='bim_id',
            field=models.CharField(max_length=100, blank=True, unique=True, null=True, verbose_name='BIM ID'),
        ),
    ]
