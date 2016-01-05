# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('racunovodstvo', '0006_auto_20160105_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='racun',
            name='oznaka',
            field=models.IntegerField(default=2015),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='racun',
            name='racunovodsko_leto',
            field=models.ForeignKey(to='core.ObdobjeLeto', default=2015),
            preserve_default=False,
        ),
    ]
