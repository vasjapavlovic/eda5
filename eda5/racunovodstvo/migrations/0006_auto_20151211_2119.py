# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('racunovodstvo', '0005_auto_20151211_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='strosek',
            name='obdobje_obracuna_leto',
            field=models.ForeignKey(default=1, to='core.ObdobjeLeto'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='strosek',
            name='obdobje_obracuna_mesec',
            field=models.ForeignKey(default=1, to='core.ObdobjeMesec'),
            preserve_default=False,
        ),
    ]
