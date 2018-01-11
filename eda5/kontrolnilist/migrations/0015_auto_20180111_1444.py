# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0003_remove_projektnomesto_tip_elementa'),
        ('kontrolnilist', '0014_auto_20180110_0735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kontrolavrednost',
            name='projektno_mesto',
        ),
        migrations.AddField(
            model_name='kontrolavrednost',
            name='projektno_mesto',
            field=models.ForeignKey(verbose_name='projektno mesto', to='deli.ProjektnoMesto', default=1),
            preserve_default=False,
        ),
    ]
