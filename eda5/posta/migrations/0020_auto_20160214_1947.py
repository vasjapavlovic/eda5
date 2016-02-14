# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0019_auto_20160120_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dokument',
            name='oznaka',
            field=models.CharField(verbose_name='številka dokumenta', max_length=50),
        ),
    ]
