# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduli', '0014_auto_20151231_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modul',
            name='oznaka',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='zavihek',
            name='oznaka',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
