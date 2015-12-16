# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduli', '0005_auto_20151216_0517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zavihek',
            name='oznaka',
            field=models.CharField(max_length=100),
        ),
    ]
