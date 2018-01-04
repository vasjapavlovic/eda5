# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kljuci', '0001_initial'),
        ('zahtevki', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='predajakljuca',
            name='zahtevek',
            field=models.ForeignKey(null=True, blank=True, to='zahtevki.Zahtevek'),
        ),
        migrations.AddField(
            model_name='kljuc',
            name='sklop_kljucev',
            field=models.ForeignKey(verbose_name='sklop ključev', to='kljuci.SklopKljucev'),
        ),
    ]
