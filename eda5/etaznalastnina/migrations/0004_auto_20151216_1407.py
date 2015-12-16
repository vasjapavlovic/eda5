# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etaznalastnina', '0003_auto_20151216_1359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lastniskaenotainterna',
            name='program',
        ),
        migrations.AddField(
            model_name='lastniskaenotaelaborat',
            name='opis',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
