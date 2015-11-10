# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lastnistvo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lastniskaskupina',
            name='program',
        ),
        migrations.DeleteModel(
            name='LastniskaSkupina',
        ),
        migrations.DeleteModel(
            name='Program',
        ),
    ]
