# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0011_obratovalniparameter_artikel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='obratovalniparameter',
            name='naziv',
        ),
        migrations.AddField(
            model_name='obratovalniparameter',
            name='enota',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='obratovalniparameter',
            name='opis',
            field=models.CharField(max_length=255, blank=True, verbose_name='opis'),
        ),
    ]
