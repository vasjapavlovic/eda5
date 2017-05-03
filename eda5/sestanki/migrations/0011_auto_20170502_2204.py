# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sestanki', '0010_auto_20170502_2202'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vnos',
            options={'verbose_name': 'vnos sestanka', 'verbose_name_plural': 'vnosi sestankov'},
        ),
    ]
