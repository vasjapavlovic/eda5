# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0003_auto_20151219_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelartikla',
            name='oznaka',
            field=models.CharField(max_length=20, default='1', unique=True),
            preserve_default=False,
        ),
    ]
