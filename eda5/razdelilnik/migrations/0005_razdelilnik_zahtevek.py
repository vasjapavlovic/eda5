# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '__first__'),
        ('razdelilnik', '0004_auto_20170717_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='razdelilnik',
            name='zahtevek',
            field=models.ForeignKey(to='zahtevki.Zahtevek', verbose_name='zahtevek', blank=True, null=True),
        ),
    ]
