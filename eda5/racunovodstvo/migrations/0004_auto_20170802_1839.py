# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racunovodstvo', '0003_racun_stavba'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='strosek',
            name='delilnik_kljuc',
        ),
        migrations.RemoveField(
            model_name='strosek',
            name='delilnik_vrsta',
        ),
        migrations.RemoveField(
            model_name='strosek',
            name='is_strosek_posameznidel',
        ),
        migrations.RemoveField(
            model_name='strosek',
            name='lastniska_skupina',
        ),
        migrations.RemoveField(
            model_name='strosek',
            name='obdobje_obracuna_leto',
        ),
        migrations.RemoveField(
            model_name='strosek',
            name='obdobje_obracuna_mesec',
        ),
    ]
