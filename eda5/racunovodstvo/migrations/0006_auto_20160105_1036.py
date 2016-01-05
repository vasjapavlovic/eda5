# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racunovodstvo', '0005_auto_20160105_0958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='racun',
            name='datum_storitve_do',
        ),
        migrations.RemoveField(
            model_name='racun',
            name='datum_storitve_od',
        ),
        migrations.RemoveField(
            model_name='racun',
            name='narocilo',
        ),
        migrations.RemoveField(
            model_name='racun',
            name='obdobje_obracuna_leto',
        ),
        migrations.RemoveField(
            model_name='racun',
            name='obdobje_obracuna_mesec',
        ),
        migrations.RemoveField(
            model_name='racun',
            name='osnova_0',
        ),
        migrations.RemoveField(
            model_name='racun',
            name='osnova_1',
        ),
        migrations.RemoveField(
            model_name='racun',
            name='osnova_2',
        ),
    ]
