# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kontrolnilist', '0009_auto_20180107_0828'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kontrolavrednost',
            options={'verbose_name_plural': 'vrednosti kontrol', 'verbose_name': 'vrednost kontrole'},
        ),
    ]
