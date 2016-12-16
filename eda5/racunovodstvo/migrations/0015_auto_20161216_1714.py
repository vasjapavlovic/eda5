# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racunovodstvo', '0014_remove_racun_obdelan_racunovodstvo'),
    ]

    operations = [
        migrations.AddField(
            model_name='racun',
            name='je_reprezentanca',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='racun',
            name='reprezentanca_opis',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
    ]
