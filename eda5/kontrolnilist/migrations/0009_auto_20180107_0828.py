# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kontrolnilist', '0008_auto_20180107_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kontrolavrednost',
            name='vrednost_text',
            field=models.CharField(blank=True, max_length=255, verbose_name='vrednost text', null=True),
        ),
    ]
