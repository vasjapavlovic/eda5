# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delovninalogi', '0011_auto_20170214_1748'),
        ('racunovodstvo', '0019_racun_zavrnjen_datum'),
    ]

    operations = [
        migrations.AddField(
            model_name='racun',
            name='opravilo',
            field=models.ForeignKey(null=True, to='delovninalogi.Opravilo', verbose_name='opravilo', blank=True),
        ),
    ]
