# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0011_auto_20151117_1019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aktivnost',
            name='id',
        ),
        migrations.AddField(
            model_name='aktivnost',
            name='id_1',
            field=models.IntegerField(primary_key=True, default=1, serialize=False),
            preserve_default=False,
        ),
    ]
