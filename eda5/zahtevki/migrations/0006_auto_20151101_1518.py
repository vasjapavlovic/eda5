# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '0005_auto_20151101_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='zahtevek',
            name='zahtevek_sestanek',
            field=models.OneToOneField(blank=True, null=True, to='zahtevki.ZahtevekSestanek'),
        ),
        migrations.AlterField(
            model_name='zahtevek',
            name='zahtevek_skodni_dogodek',
            field=models.OneToOneField(blank=True, null=True, to='zahtevki.ZahtevekSkodniDogodek'),
        ),
    ]
