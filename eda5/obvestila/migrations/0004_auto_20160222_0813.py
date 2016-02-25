# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0004_auto_20160105_1048'),
        ('obvestila', '0003_auto_20160222_0807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='obvestilo',
            name='user',
        ),
        migrations.AddField(
            model_name='obvestilo',
            name='oseba',
            field=models.ForeignKey(to='partnerji.Oseba', default=1),
            preserve_default=False,
        ),
    ]
