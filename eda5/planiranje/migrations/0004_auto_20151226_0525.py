# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planiranje', '0003_planiranoopravilo_datum_izvajanja'),
    ]

    operations = [
        migrations.RenameField(
            model_name='planiranoopravilo',
            old_name='datum_izvajanja',
            new_name='datum_prve_izvedbe',
        ),
    ]
