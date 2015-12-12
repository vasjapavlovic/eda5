# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0009_auto_20151211_2059'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skupinapartnerjev',
            options={'verbose_name_plural': 'skupine partnerjev', 'ordering': ['naziv'], 'verbose_name': 'skupina partnerjev'},
        ),
    ]
