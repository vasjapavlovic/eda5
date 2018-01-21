# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kontrolnilist', '0035_auto_20180121_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kontrolavrednost',
            name='vrednost_yes_no',
            field=models.IntegerField(choices=[(1, 'DA'), (-1, 'NE')], null=True, verbose_name='vrednost DA/NE', blank=True),
        ),
    ]
