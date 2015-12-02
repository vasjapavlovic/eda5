# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0007_artikelplan_planirano_opravilo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artikelplan',
            old_name='element',
            new_name='artikel',
        ),
        migrations.RemoveField(
            model_name='artikelplan',
            name='planirano_opravilo',
        ),
    ]
