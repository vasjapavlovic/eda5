# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduli', '0010_auto_20151225_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='modul',
            name='zap_st',
            field=models.IntegerField(default=0, verbose_name='zaporedna številka'),
        ),
    ]
