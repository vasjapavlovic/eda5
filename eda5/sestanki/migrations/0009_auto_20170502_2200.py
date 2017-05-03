# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sestanki', '0008_auto_20170502_2158'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vnos',
            options={'verbose_name_plural': 'vnosi sestankov', 'ordering': ['self__pk'], 'verbose_name': 'vnos sestanka'},
        ),
    ]
