# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pomanjkljivosti', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pomanjkljivost',
            name='etaza',
            field=models.CharField(max_length=50, default='K1'),
            preserve_default=False,
        ),
    ]
