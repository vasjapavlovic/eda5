# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planiranje', '0005_auto_20151201_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planopravilo',
            name='plan',
            field=models.ForeignKey(to='planiranje.PlanIzdaja'),
        ),
    ]
