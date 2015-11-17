# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '0006_remove_zahtevek_dokument'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zahteveksestanek',
            name='zapisnik',
        ),
        migrations.RemoveField(
            model_name='zahtevekskodnidogodek',
            name='dokazno_gradivo',
        ),
        migrations.RemoveField(
            model_name='zahtevekskodnidogodek',
            name='dokument_poravnava',
        ),
        migrations.RemoveField(
            model_name='zahtevekskodnidogodek',
            name='dokument_prijava_skode',
        ),
        migrations.RemoveField(
            model_name='zahtevekskodnidogodek',
            name='dokument_zapisnik_ogleda',
        ),
    ]
