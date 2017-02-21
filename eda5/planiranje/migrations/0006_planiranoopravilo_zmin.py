# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planiranje', '0005_plan_zahtevek'),
    ]

    operations = [
        migrations.AddField(
            model_name='planiranoopravilo',
            name='zmin',
            field=models.IntegerField(default=15, verbose_name='zaokrožitev [min]'),
        ),
    ]
