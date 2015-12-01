# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arhiv', '0002_auto_20151122_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arhiviranje',
            name='created',
            field=models.DateTimeField(null=True, auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='arhiviranje',
            name='updated',
            field=models.DateTimeField(null=True, auto_now=True),
        ),
    ]
