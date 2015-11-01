# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delovninalogi', '0003_auto_20151101_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='delo',
            name='time_stop',
            field=models.TimeField(verbose_name='Ura:Končano', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='delo',
            name='time_start',
            field=models.TimeField(verbose_name='Ura:Začeto', blank=True, null=True),
        ),
    ]
