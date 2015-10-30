# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etaznalastnina', '0006_auto_20151030_0021'),
    ]

    operations = [
        migrations.AddField(
            model_name='lastniskaskupina',
            name='lastniska_enota',
            field=models.ManyToManyField(to='etaznalastnina.LastniskaEnotaInterna', blank=True),
        ),
    ]
