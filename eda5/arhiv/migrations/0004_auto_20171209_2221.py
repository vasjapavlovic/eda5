# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '__first__'),
        ('razdelilnik', '0001_initial'),
        ('reklamacije', '__first__'),
        ('arhiv', '0003_arhiviranje_racun'),
        ('sestanki', '__first__'),
    ]

    operations = [
        migrations.AddField(
            model_name='arhiviranje',
            name='razdelilnik',
            field=models.ForeignKey(null=True, blank=True, to='razdelilnik.Razdelilnik'),
        ),
        migrations.AddField(
            model_name='arhiviranje',
            name='reklamacija',
            field=models.ForeignKey(null=True, blank=True, to='reklamacije.Reklamacija'),
        ),
        migrations.AddField(
            model_name='arhiviranje',
            name='sestanek',
            field=models.ForeignKey(null=True, blank=True, to='sestanki.Sestanek'),
        ),
        migrations.AddField(
            model_name='arhiviranje',
            name='zahtevek',
            field=models.ForeignKey(null=True, blank=True, to='zahtevki.Zahtevek'),
        ),
    ]
