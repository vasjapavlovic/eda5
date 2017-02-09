# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '0009_auto_20170208_2108'),
        ('narocila', '0004_auto_20170208_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='narocilo',
            name='zahtevek',
            field=models.ForeignKey(blank=True, to='zahtevki.Zahtevek', null=True),
        ),
    ]
