# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etaznalastnina', '0007_lastniskaskupina_lastniska_enota'),
    ]

    operations = [
        migrations.AddField(
            model_name='lastniskaenotainterna',
            name='lastniski_delez',
            field=models.DecimalField(max_digits=5, verbose_name='lastniški delež', decimal_places=4, blank=True, default=0.001),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lastniskaenotainterna',
            name='st_oseb',
            field=models.IntegerField(verbose_name='število oseb', blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lastniskaenotainterna',
            name='povrsina_tlorisna_neto',
            field=models.CharField(max_length=4, verbose_name='neto tlorisna površina', blank=True),
        ),
    ]
