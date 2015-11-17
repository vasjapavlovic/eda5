# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arhiv', '0004_auto_20151117_0654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arhivmesto',
            name='zahtevek',
        ),
    ]
