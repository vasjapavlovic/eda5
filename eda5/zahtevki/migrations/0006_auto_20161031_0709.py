# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahtevki', '0005_auto_20160225_2230'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='zahtevek',
            options={'verbose_name_plural': 'zahtevki', 'ordering': ('-id',), 'verbose_name': 'zahtevek'},
        ),
    ]
