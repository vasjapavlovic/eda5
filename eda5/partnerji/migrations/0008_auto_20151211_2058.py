# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0007_auto_20151211_1604'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='partner',
            options={'verbose_name_plural': 'partnerji', 'ordering': ('kratko_ime',), 'verbose_name': 'partner'},
        ),
    ]
