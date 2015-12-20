# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arhiv', '0002_auto_20151215_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arhiv',
            name='oznaka',
            field=models.CharField(verbose_name='oznaka', max_length=10, unique=True),
        ),
    ]
