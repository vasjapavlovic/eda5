# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0002_auto_20151215_1854'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='oseba',
            options={'ordering': ['priimek'], 'verbose_name': 'Oseba', 'verbose_name_plural': 'Osebe'},
        ),
    ]
