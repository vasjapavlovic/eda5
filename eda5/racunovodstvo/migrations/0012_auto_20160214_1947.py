# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racunovodstvo', '0011_auto_20160212_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='strosek',
            name='osnova',
            field=models.DecimalField(verbose_name='osnova za ddv', decimal_places=5, max_digits=10),
        ),
    ]
