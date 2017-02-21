# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0005_auto_20170207_1457'),
        ('pomanjkljivosti', '0009_auto_20170220_2051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pomanjkljivost',
            name='element',
        ),
        migrations.AddField(
            model_name='pomanjkljivost',
            name='element',
            field=models.ManyToManyField(to='deli.ProjektnoMesto', blank=True, verbose_name='element'),
        ),
    ]
