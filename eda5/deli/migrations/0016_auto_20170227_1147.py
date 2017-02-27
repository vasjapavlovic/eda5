# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0015_delstavbe_bim_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delstavbe',
            name='oznaka',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
