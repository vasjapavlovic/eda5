# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naloge', '0001_initial'),
        ('sestanki', '0001_initial'),
        ('zahtevki', '0001_initial'),
        ('partnerji', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='naloga',
            name='nosilec',
            field=models.ForeignKey(verbose_name='nosilec', to='partnerji.Oseba'),
        ),
        migrations.AddField(
            model_name='naloga',
            name='vnos_sestanka',
            field=models.ForeignKey(null=True, blank=True, verbose_name='sklep sestanka', to='sestanki.Vnos'),
        ),
        migrations.AddField(
            model_name='naloga',
            name='zahtevek',
            field=models.ForeignKey(null=True, blank=True, verbose_name='Rešuje se pod Zahtevkom', to='zahtevki.Zahtevek'),
        ),
    ]
