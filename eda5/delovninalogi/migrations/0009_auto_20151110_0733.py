# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delovninalogi', '0008_opravilo_nadzornik'),
    ]

    operations = [
        migrations.RenameField(
            model_name='delovninalog',
            old_name='date_plan',
            new_name='datum_plan',
        ),
    ]
