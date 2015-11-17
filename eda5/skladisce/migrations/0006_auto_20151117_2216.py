# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skladisce', '0005_auto_20151117_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dnevnik',
            name='stopnja_ddv',
            field=models.DecimalField(decimal_places=3, max_digits=4),
        ),
    ]
