# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0002_auto_20151215_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delstavbe',
            name='oznaka',
            field=models.CharField(unique=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='projektnomesto',
            name='oznaka',
            field=models.CharField(unique=True, max_length=20),
        ),
    ]
