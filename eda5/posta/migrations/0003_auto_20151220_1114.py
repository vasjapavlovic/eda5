# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0002_auto_20151220_1113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skupinadokumenta',
            name='created',
        ),
        migrations.RemoveField(
            model_name='skupinadokumenta',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='vrstadokumenta',
            name='created',
        ),
        migrations.RemoveField(
            model_name='vrstadokumenta',
            name='updated',
        ),
    ]
