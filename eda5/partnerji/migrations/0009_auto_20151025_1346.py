# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0008_auto_20151025_1341'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trracun',
            old_name='trr',
            new_name='iban',
        ),
    ]
