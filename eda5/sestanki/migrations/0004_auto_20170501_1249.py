# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sestanki', '0003_auto_20170410_1800'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tema',
            new_name='Zadeva',
        ),
        migrations.AlterModelOptions(
            name='zadeva',
            options={'verbose_name_plural': 'zadeve', 'verbose_name': 'zadeva'},
        ),
    ]
