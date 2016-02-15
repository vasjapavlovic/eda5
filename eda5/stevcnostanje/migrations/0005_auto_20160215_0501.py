# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stevcnostanje', '0004_delilnik_opis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delilnik',
            name='meritev',
            field=models.IntegerField(choices=[(1, 'Toplota [MWh]'), (2, 'Hlad [MWh]'), (3, 'Topla voda [m3]'), (4, 'Hladna voda [m3]'), (5, 'Elektrika [kWh]')]),
        ),
    ]
