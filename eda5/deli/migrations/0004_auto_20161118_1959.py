# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0003_auto_20151229_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='delstavbe',
            name='funkcija',
            field=models.CharField(max_length=255, verbose_name='funkcija sistema', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='projektnomesto',
            name='funkcija',
            field=models.CharField(max_length=255, verbose_name='funkcija elementa', null=True, blank=True),
        ),
    ]
