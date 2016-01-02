# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lastnistvo', '0005_auto_20160101_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predajalastnine',
            name='lastniska_enota_interna',
            field=models.ManyToManyField(to='etaznalastnina.LastniskaEnotaInterna', blank=True, related_name='lastniska_enota_interna', verbose_name='LE interna'),
        ),
    ]
