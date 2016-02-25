# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obvestila', '0002_komentar_obvestilo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='obvestilo',
            old_name='onaka',
            new_name='oznaka',
        ),
    ]
