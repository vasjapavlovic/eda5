# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('narocila', '0003_narocilo_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='narocilo',
            name='status',
        ),
    ]
