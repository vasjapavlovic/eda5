# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stevci', '0004_auto_20151105_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='odcitek',
            name='id',
            field=models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True),
        ),
    ]
