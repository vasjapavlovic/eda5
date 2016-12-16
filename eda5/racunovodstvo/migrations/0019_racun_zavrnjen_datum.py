# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racunovodstvo', '0018_auto_20161216_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='racun',
            name='zavrnjen_datum',
            field=models.DateField(blank=True, null=True),
        ),
    ]
