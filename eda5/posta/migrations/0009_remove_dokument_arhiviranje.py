# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0008_auto_20151116_2047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dokument',
            name='arhiviranje',
        ),
    ]