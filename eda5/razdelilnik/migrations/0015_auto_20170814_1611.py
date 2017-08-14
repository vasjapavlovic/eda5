# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('razdelilnik', '0014_auto_20170810_0538'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='strosekrazdelilnikpostavka',
            options={'verbose_name_plural': 'StrosekRazdelilnikPostavke', 'ordering': ('oznaka',), 'verbose_name': 'StrosekRazdelilnikPostavka'},
        ),
    ]
