# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kontrolnilist', '0002_auto_20180106_1007'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OpcijaSelect',
            new_name='KontrolaSpecifikacijaOpcijaSelect',
        ),
    ]
