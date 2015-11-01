# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '0002_auto_20151101_1458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zahtevek',
            name='zahtevek_sestanek',
        ),
        migrations.AlterField(
            model_name='zahtevek',
            name='zahtevek_skodni_dogodek',
            field=models.OneToOneField(default=1, to='zahtevki.ZahtevekSkodniDogodek'),
            preserve_default=False,
        ),
    ]
