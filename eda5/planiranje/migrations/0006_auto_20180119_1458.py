# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0004_delstavbe_stavba'),
        ('planiranje', '0005_auto_20180118_1701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planaktivnost',
            name='projektno_mesto',
        ),
        migrations.AddField(
            model_name='plankontrolaspecifikacija',
            name='projektno_mesto',
            field=models.ManyToManyField(to='deli.ProjektnoMesto', blank=True, verbose_name='projektno mesto'),
        ),
    ]
