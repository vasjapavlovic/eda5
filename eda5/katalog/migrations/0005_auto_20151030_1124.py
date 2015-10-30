# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0004_auto_20151030_0035'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modelartikla',
            old_name='dokumentacija',
            new_name='prejeta_dokumentacija',
        ),
    ]
