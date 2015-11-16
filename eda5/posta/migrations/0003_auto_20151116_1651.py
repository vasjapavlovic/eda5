# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0002_auto_20151116_1642'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aktivnost',
            options={'verbose_name': 'aktivnost', 'verbose_name_plural': 'aktivnosti'},
        ),
    ]
