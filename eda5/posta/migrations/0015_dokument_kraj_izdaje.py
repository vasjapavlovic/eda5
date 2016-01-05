# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0014_remove_aktivnost_likvidiral'),
    ]

    operations = [
        migrations.AddField(
            model_name='dokument',
            name='kraj_izdaje',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
