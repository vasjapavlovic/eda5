# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racunovodstvo', '0017_racun_zavrnjen_obrazlozitev_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='racun',
            name='zavrnjen_obrazlozitev_text',
            field=models.TextField(null=True, blank=True),
        ),
    ]
