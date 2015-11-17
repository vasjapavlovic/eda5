# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delstavbe',
            name='prejeta_dokumentacija',
        ),
        migrations.RemoveField(
            model_name='element',
            name='prejeta_dokumentacija',
        ),
    ]
