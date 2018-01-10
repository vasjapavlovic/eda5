# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kontrolnilist', '0013_auto_20180110_0724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kontrolavrednost',
            name='projektno_mesto',
            field=models.ManyToManyField(to='deli.ProjektnoMesto', verbose_name='projektno mesto', blank=True),
        ),
    ]
