# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skladisce', '0002_artikel_dobavitelj'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dnevnik',
            old_name='nabavna_vrednost',
            new_name='cena',
        ),
    ]
