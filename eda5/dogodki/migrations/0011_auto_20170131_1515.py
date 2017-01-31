# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogodki', '0010_auto_20161126_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dogodek',
            name='zahtevek',
            field=models.ForeignKey(to='zahtevki.Zahtevek'),
        ),
    ]
