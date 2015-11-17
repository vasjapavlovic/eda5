# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '0005_auto_20151117_0514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zahtevek',
            name='dokument',
        ),
    ]
