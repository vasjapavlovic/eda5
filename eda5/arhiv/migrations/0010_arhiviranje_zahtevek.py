# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '0004_auto_20160102_1407'),
        ('arhiv', '0009_remove_arhiviranje_zahtevek'),
    ]

    operations = [
        migrations.AddField(
            model_name='arhiviranje',
            name='zahtevek',
            field=models.ForeignKey(to='zahtevki.Zahtevek', null=True, blank=True),
        ),
    ]
