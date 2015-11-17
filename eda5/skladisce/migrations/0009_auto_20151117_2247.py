# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skladisce', '0008_auto_20151117_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dnevnik',
            name='cena',
            field=models.DecimalField(max_digits=6, null=True, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='dnevnik',
            name='stopnja_ddv',
            field=models.DecimalField(max_digits=4, null=True, decimal_places=3, blank=True),
        ),
    ]
