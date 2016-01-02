# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '0003_auto_20151230_1657'),
        ('planiranje', '0004_auto_20151226_0525'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='zahtevek',
            field=models.ForeignKey(blank=True, to='zahtevki.Zahtevek', null=True),
        ),
    ]
