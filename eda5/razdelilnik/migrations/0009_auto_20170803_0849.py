# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('razdelilnik', '0008_auto_20170803_0835'),
    ]

    operations = [
        migrations.AddField(
            model_name='strosekdelitevvrsta',
            name='skrajsan_naziv',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='strosekkljucdelitve',
            name='skrajsan_naziv',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
    ]
