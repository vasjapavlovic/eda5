# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='skupinadokumenta',
            name='zap_st',
            field=models.IntegerField(verbose_name='zaporedna številka', default=0),
        ),
        migrations.AlterField(
            model_name='vrstadokumenta',
            name='zap_st',
            field=models.IntegerField(verbose_name='zaporedna številka', default=0),
        ),
    ]
