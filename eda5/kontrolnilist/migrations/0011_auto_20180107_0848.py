# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kontrolnilist', '0010_auto_20180107_0835'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kontrolaspecifikacija',
            old_name='vrsta_vnosa',
            new_name='vrednost_vrsta',
        ),
    ]
