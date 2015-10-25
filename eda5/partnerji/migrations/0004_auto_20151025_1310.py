# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0003_auto_20151025_1306'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drzava',
            old_name='oznaka',
            new_name='iso_koda',
        ),
    ]
