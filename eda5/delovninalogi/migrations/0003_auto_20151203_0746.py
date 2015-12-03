# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delovninalogi', '0002_auto_20151203_0301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='delovrsta',
            old_name='sklo',
            new_name='sklop',
        ),
    ]
