# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kljuci', '0008_auto_20161126_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='predajakljuca',
            name='datum_vracila',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='predajakljuca',
            name='opis_vracila',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
