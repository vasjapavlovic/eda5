# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0006_auto_20151220_1500'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vrstadokumenta',
            options={'ordering': ('oznaka',), 'verbose_name_plural': 'Vrste Dokumentov', 'verbose_name': 'Vrsta Dokumenta'},
        ),
    ]
