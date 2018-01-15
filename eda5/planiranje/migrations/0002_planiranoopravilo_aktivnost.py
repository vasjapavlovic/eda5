# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kontrolnilist', '0015_auto_20180111_1444'),
        ('planiranje', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='planiranoopravilo',
            name='aktivnost',
            field=models.ManyToManyField(blank=True, to='kontrolnilist.Aktivnost'),
        ),
    ]
