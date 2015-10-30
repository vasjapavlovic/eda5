# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('narocila', '0004_auto_20151030_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='narocilopogodba',
            name='predmet_pogodbe',
            field=models.CharField(blank=True, max_length=255, verbose_name='številka pogodbe'),
        ),
    ]
