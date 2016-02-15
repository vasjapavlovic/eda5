# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stevcnostanje', '0003_auto_20160214_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='delilnik',
            name='opis',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
