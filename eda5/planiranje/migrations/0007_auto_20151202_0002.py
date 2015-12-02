# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planiranje', '0006_auto_20151202_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planopravilo',
            name='plan',
            field=models.ForeignKey(to='planiranje.Plan'),
        ),
    ]
