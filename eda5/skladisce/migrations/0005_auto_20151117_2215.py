# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skladisce', '0004_auto_20151117_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dnevnik',
            name='stopnja_ddv',
            field=models.DecimalField(max_digits=4, choices=[('0.095', '9,5%'), ('0.20', '22,0%')], decimal_places=3),
        ),
    ]
