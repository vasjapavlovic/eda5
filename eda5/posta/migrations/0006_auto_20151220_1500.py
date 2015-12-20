# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0005_auto_20151220_1445'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aktivnost',
            old_name='datum',
            new_name='datum_aktivnosti',
        ),
        migrations.RenameField(
            model_name='dokument',
            old_name='datum',
            new_name='datum_dokumenta',
        ),
    ]
