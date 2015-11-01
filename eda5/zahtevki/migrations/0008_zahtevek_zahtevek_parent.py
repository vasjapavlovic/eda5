# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '0007_auto_20151101_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='zahtevek',
            name='zahtevek_parent',
            field=models.ForeignKey(blank=True, to='zahtevki.Zahtevek', null=True),
        ),
    ]
