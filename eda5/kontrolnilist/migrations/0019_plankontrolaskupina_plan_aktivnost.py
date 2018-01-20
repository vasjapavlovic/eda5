# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kontrolnilist', '0018_auto_20180116_0724'),
    ]

    operations = [
        migrations.AddField(
            model_name='plankontrolaskupina',
            name='plan_aktivnost',
            field=models.ForeignKey(verbose_name='planirana aktivnost', default=1, to='kontrolnilist.PlanAktivnost'),
            preserve_default=False,
        ),
    ]
