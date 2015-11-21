# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delovninalogi', '0004_auto_20151121_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delo',
            name='time_start',
            field=models.DurationField(verbose_name='Ura:Začeto', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='delo',
            name='time_stop',
            field=models.DurationField(verbose_name='Ura:Končano', null=True, blank=True),
        ),
    ]
