# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '0008_auto_20161101_1613'),
        ('kljuci', '0007_auto_20161126_1113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='predajakljuca',
            name='predaja_lastnine',
        ),
        migrations.AddField(
            model_name='predajakljuca',
            name='zahtevek',
            field=models.ForeignKey(null=True, blank=True, to='zahtevki.Zahtevek'),
        ),
    ]
