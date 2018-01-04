# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogodki', '0001_initial'),
        ('zahtevki', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dogodek',
            name='zahtevek',
            field=models.ForeignKey(to='zahtevki.Zahtevek'),
        ),
    ]
