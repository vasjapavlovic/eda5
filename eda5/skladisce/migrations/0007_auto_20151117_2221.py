# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skladisce', '0006_auto_20151117_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dnevnik',
            name='stopnja_ddv',
            field=models.DecimalField(decimal_places=3, choices=[(0.095, '9,5%'), (0.2, '22,0%')], max_digits=4),
        ),
    ]
