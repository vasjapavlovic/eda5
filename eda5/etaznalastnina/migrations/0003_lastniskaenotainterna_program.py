# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etaznalastnina', '0002_lastniskaenotaelaborat_posta'),
    ]

    operations = [
        migrations.AddField(
            model_name='lastniskaenotainterna',
            name='program',
            field=models.CharField(max_length=50, default='stanovanje'),
            preserve_default=False,
        ),
    ]
