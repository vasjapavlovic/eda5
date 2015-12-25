# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduli', '0007_modul_parent_modul'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modul',
            old_name='parent_modul',
            new_name='parent',
        ),
    ]
