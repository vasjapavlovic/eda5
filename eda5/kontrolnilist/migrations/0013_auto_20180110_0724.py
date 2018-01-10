# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0003_remove_projektnomesto_tip_elementa'),
        ('kontrolnilist', '0012_auto_20180107_0849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kontrolavrednost',
            name='projektno_mesto',
        ),
        migrations.AddField(
            model_name='kontrolavrednost',
            name='projektno_mesto',
            field=models.ManyToManyField(to='deli.ProjektnoMesto', verbose_name='projektno mesto'),
        ),
    ]
