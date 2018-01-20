# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predpisi', '0001_initial'),
        ('planiranje', '0003_remove_planiranoopravilo_aktivnost'),
    ]

    operations = [
        migrations.AddField(
            model_name='planiranoopravilo',
            name='osnova',
            field=models.ForeignKey(to='predpisi.PredpisSklop', null=True, blank=True),
        ),
    ]
