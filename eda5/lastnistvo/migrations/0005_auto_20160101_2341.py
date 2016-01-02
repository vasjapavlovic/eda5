# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etaznalastnina', '0016_auto_20160101_2333'),
        ('lastnistvo', '0004_auto_20160101_2252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='predajalastnine',
            name='lastniska_enota',
        ),
        migrations.AddField(
            model_name='predajalastnine',
            name='lastniska_enota_elaborat',
            field=models.ManyToManyField(verbose_name='LE elaborat', blank=True, to='etaznalastnina.LastniskaEnotaElaborat'),
        ),
        migrations.AddField(
            model_name='predajalastnine',
            name='lastniska_enota_interna',
            field=models.ManyToManyField(related_name='LE_interna', verbose_name='LE interna', blank=True, to='etaznalastnina.LastniskaEnotaInterna'),
        ),
    ]
