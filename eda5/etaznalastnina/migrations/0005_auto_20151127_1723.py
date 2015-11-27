# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etaznalastnina', '0004_auto_20151127_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='lastniskaenotaelaborat',
            name='povrsina_tlorisna_neto',
            field=models.DecimalField(default=1.1, verbose_name='neto tlorisna površina', max_digits=6, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lastniskaenotainterna',
            name='povrsina_tlorisna_neto',
            field=models.DecimalField(default=1.1, verbose_name='neto tlorisna površina', max_digits=6, decimal_places=2),
            preserve_default=False,
        ),
    ]
