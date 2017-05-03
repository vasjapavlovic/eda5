# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sestanki', '0009_auto_20170502_2200'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vnos',
            options={'ordering': ['opis'], 'verbose_name_plural': 'vnosi sestankov', 'verbose_name': 'vnos sestanka'},
        ),
    ]
