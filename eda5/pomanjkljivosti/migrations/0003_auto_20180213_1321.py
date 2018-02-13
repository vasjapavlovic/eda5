# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arhiv', '0002_auto_20180126_2341'),
        ('zaznamki', '0001_initial'),
        ('pomanjkljivosti', '0002_auto_20180213_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='pomanjkljivost',
            name='gradivo',
            field=models.ManyToManyField(blank=True, verbose_name='Gradivo', to='arhiv.Arhiviranje'),
        ),
        migrations.AddField(
            model_name='pomanjkljivost',
            name='gradivo_zaznamek',
            field=models.ManyToManyField(blank=True, verbose_name='Gradivo - Zaznamek', to='zaznamki.Zaznamek'),
        ),
    ]
