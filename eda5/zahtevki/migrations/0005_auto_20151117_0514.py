# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '0004_auto_20151116_1642'),
    ]

    operations = [
        migrations.RenameField(
            model_name='zahtevek',
            old_name='predmet',
            new_name='naziv',
        ),
    ]
