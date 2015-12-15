# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racunovodstvo', '0006_auto_20151211_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='konto',
            name='zap_st',
            field=models.IntegerField(verbose_name='zaporedna Številka', default=0),
        ),
    ]
