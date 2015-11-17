# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '0006_remove_zahtevek_dokument'),
        ('arhiv', '0002_arhiviranje_dokument'),
    ]

    operations = [
        migrations.AddField(
            model_name='arhivmesto',
            name='zahtevek',
            field=models.OneToOneField(to='zahtevki.Zahtevek', null=True, blank=True),
        ),
    ]
