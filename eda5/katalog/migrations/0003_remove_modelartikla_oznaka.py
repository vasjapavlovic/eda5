# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0002_auto_20151127_2312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modelartikla',
            name='oznaka',
        ),
    ]
