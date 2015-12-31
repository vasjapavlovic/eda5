# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0012_auto_20151229_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skupinadokumenta',
            name='zap_st',
            field=models.IntegerField(default=9999, verbose_name='zaporedna številka'),
        ),
        migrations.AlterField(
            model_name='vrstadokumenta',
            name='zap_st',
            field=models.IntegerField(default=9999, verbose_name='zaporedna številka'),
        ),
    ]
