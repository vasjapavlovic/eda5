# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0007_dokument_likvidiran'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dokument',
            old_name='likvidiran',
            new_name='is_likvidiran',
        ),
    ]
