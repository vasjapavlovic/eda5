# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '0003_auto_20151101_1511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zahtevekskodnidogodek',
            name='predvidena_skoda',
        ),
        migrations.AddField(
            model_name='zahtevekskodnidogodek',
            name='predvidena_visina_skode',
            field=models.DecimalField(max_digits=7, blank=True, decimal_places=2, verbose_name='predvidena višina škode', default=1000),
            preserve_default=False,
        ),
    ]
