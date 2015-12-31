# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delovninalogi', '0003_opravilo_planirano_opravilo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='opravilo',
            old_name='nadzornik',
            new_name='nosilec',
        ),
    ]
