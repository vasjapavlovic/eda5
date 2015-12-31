# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predpisi', '0002_auto_20151227_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predpissklop',
            name='zap_st',
            field=models.IntegerField(default=9999, verbose_name='zaporedna številka'),
        ),
    ]
