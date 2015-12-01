# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0006_auto_20151201_1721'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projektnomesto',
            options={'ordering': ['oznaka'], 'verbose_name': 'projektno mesto', 'verbose_name_plural': 'projektna mesta'},
        ),
    ]
