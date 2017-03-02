# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0022_auto_20170208_2108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aktivnost',
            name='vrsta_aktivnosti',
        ),
    ]
