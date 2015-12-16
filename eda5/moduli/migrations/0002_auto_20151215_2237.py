# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduli', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modul',
            old_name='url_name',
            new_name='barva',
        ),
    ]
