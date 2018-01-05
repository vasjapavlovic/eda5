# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0003_remove_projektnomesto_tip_elementa'),
        ('delovninalogi', '0006_auto_20180105_0849'),
    ]

    operations = [
        migrations.AddField(
            model_name='aktivnost',
            name='projektno_mesto',
            field=models.ManyToManyField(to='deli.ProjektnoMesto', blank=True, verbose_name='projektno mesto'),
        ),
    ]
