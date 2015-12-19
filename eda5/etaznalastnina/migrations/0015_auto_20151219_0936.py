# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etaznalastnina', '0014_auto_20151218_0904'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='internadodatno',
            options={'ordering': ['interna'], 'verbose_name': 'dodatek interni LE', 'verbose_name_plural': 'dodatki internim LE'},
        ),
    ]
