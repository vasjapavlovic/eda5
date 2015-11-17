# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arhiv', '0003_arhivmesto_zahtevek'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arhivmesto',
            name='zahtevek',
            field=models.OneToOneField(to='zahtevki.Zahtevek'),
        ),
    ]
