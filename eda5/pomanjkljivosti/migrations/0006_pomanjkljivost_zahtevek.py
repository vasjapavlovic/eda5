# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '0009_auto_20170208_2108'),
        ('pomanjkljivosti', '0005_auto_20170214_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='pomanjkljivost',
            name='zahtevek',
            field=models.ForeignKey(null=True, blank=True, to='zahtevki.Zahtevek'),
        ),
    ]
