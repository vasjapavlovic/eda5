# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0009_auto_20151225_1801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dokument',
            name='oznaka_baza',
        ),
    ]
