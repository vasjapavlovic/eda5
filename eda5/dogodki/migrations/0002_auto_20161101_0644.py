# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogodki', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dogodek',
            options={'verbose_name_plural': 'dogodki', 'verbose_name': 'dogodek'},
        ),
    ]
