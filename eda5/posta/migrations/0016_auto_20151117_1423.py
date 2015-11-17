# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0015_auto_20151117_1411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dokument',
            name='artikel',
        ),
        migrations.RemoveField(
            model_name='dokument',
            name='delovninalog',
        ),
        migrations.RemoveField(
            model_name='dokument',
            name='delstavbe',
        ),
        migrations.RemoveField(
            model_name='dokument',
            name='element',
        ),
        migrations.RemoveField(
            model_name='dokument',
            name='narocilo',
        ),
        migrations.RemoveField(
            model_name='dokument',
            name='zahtevek',
        ),
    ]
