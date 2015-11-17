# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0009_remove_dokument_arhiviranje'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aktivnost',
            old_name='aktivnost',
            new_name='vrsta_aktivnosti',
        ),
    ]
