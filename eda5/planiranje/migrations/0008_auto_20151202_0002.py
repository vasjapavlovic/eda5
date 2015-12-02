# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planiranje', '0007_auto_20151202_0002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planizdaja',
            name='plan',
        ),
        migrations.DeleteModel(
            name='PlanIzdaja',
        ),
    ]
