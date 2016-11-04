# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '0007_auto_20161101_1522'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='zahtevek',
            options={'verbose_name_plural': 'zahtevki', 'ordering': ('-pk',), 'verbose_name': 'zahtevek'},
        ),
    ]
