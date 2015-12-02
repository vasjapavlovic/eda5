# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planiranje', '0010_auto_20151202_0013'),
    ]

    operations = [
        migrations.AddField(
            model_name='planiranaaktivnost',
            name='naziv_opravila_izven_plana',
            field=models.CharField(max_length=255, default='abc'),
            preserve_default=False,
        ),
    ]
