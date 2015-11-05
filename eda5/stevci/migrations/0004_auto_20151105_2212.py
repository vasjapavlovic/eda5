# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stevci', '0003_odcitek_odcital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='odcitek',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
