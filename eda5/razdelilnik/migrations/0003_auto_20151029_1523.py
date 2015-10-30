# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etaznalastnina', '0003_auto_20151029_1523'),
        ('racunovodstvo', '0008_auto_20151029_1501'),
        ('razdelilnik', '0002_auto_20151029_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='strosekle',
            name='lastniska_enota',
            field=models.ForeignKey(default=1, to='etaznalastnina.LastniskaEnotaInterna'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='strosekle',
            name='strosek',
            field=models.ForeignKey(default=1, to='racunovodstvo.Strosek'),
            preserve_default=False,
        ),
    ]
