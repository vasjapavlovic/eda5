# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racunovodstvo', '0016_racun_zavrnjen'),
    ]

    operations = [
        migrations.AddField(
            model_name='racun',
            name='zavrnjen_obrazlozitev_text',
            field=models.CharField(null=True, blank=True, max_length=255),
        ),
    ]
